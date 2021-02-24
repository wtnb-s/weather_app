<?php
namespace App\Controller;
use App\Controller\AppController;
use Cake\Core\Configure;
use Cake\Utility\Hash;

class MapController extends AppController {
    public function initialize() {
        parent::initialize();
        $this->loadModel('City');
    }

    public function index() {
        // 年リスト取得
        foreach (range(1900,2020) as $i){
            $yearList[$i] = $i . "年";
        }
        // 月リスト取得
        foreach (range(1,12) as $i){
            $monthList[$i] = $i . "月";
        }
        // 表示要素リスト取得
        $variableList = Configure::read('variableList');
        // 都市名リスト取得
        $cityList = $this->City->getList();
        $this->set(compact('yearList', 'monthList', 'variableList', 'cityList'));

        // 画像作成に必要なパラメータをクエリ パラメータから取得
        $data['fromYear'] = $this->request->query('fromYear');
        $data['toYear'] = $this->request->query('toYear');
        $data['month'] = $this->request->query('month');
        $data['variable'] = $this->request->query('variable');
        $data['analysisType'] = $this->request->query('analysisType');
    
        // APIから画像を取得
        $url = "flask:5000/apiGetPlotMap?fromYear={$data['fromYear']}&toYear={$data['toYear']}&month={$data['month']}&variable={$data['variable']}&analysisType={$data['analysisType']}";
        $result = $this->__getImageFromUrl($url);

        if (!empty($result)) {
            $data['image'] = TMP_IMG;
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
        curl_setopt($ch, CURLOPT_HEADER, false );
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $raw = curl_exec($ch); 
        curl_close($ch);
        $fp = fopen(IMG_PATH . TMP_IMG, 'w');
        fwrite($fp, $raw);
        fclose($fp);
        return true;
    }
}