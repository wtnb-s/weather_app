<?php
namespace App\Controller;
use App\Controller\AppController;
use Cake\Core\Configure;
use Cake\Utility\Hash;

class LocationController extends AppController { 
    public function initialize() {
        parent::initialize();
        $this->loadModel('City');
    }

    public function index() {
        // 都市名リスト取得
        $cityList = Hash::combine($this->City->getList(),'{n}.city_alpha', '{n}.city_name');
        // 月リスト取得
        foreach (range(1,12) as $i){
            $monthList[$i] = $i . "月";
        }
        // 表示要素リスト取得
        $variableList = Configure::read('variableList');
        // 移動平均期間リスト取得
        foreach (range(1,20) as $i){
            $period[$i] = $i . "期間";
        }
        $this->set(compact('cityList', 'monthList', 'variableList', 'period'));

        // 画像作成に必要なパラメータをクエリ パラメータから取得
        $city = $this->request->query('city');
        $month = $this->request->query('month');
        $variable = $this->request->query('variable');
        $runningMeanPeriod = !empty($this->request->query('runningMeanPeriod')) ? $this->request->query('runningMeanPeriod') : 0;
        // APIから画像を取得
        $url = "flask:5000/apiGetLineGraph?city={$city}&month={$month}&variable={$variable}&runningMeanPeriod={$runningMeanPeriod}";
        $result = $this->__getImageFromUrl($url);

        $data=[];
        if (!empty($result)) {
            $data['image'] = TMP_IMG;
            $data['city'] = $cityList[$city];
        }
        $this->set(compact('data'));
    }

    /*
    * URLから画像を取得し保存する
    * param string $url 画像URL
    */
    private function __getImageFromUrl(string $url) {
        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_TIMEOUT, 3);
        curl_setopt( $ch, CURLOPT_HEADER, false );
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $raw = curl_exec($ch); 
        curl_close($ch);
        $fp = fopen(IMG_PATH . TMP_IMG, 'w');
        fwrite($fp, $raw);
        fclose($fp);
        return true;
    }

}