<?php
namespace App\Controller;
use App\Controller\AppController;
use Cake\Core\Configure;

class TempertureController extends AppController {
    public function initialize() {
        parent::initialize();
    }

    public function index() {
        // 都市かなリスト取得
        $cityKana = Configure::read('cityKana');

        // 選択場所リスト取得
        $dirList = glob(PYTHON_DATA_TEMP . '*');
        foreach($dirList as $dir) {
            $cityName = basename($dir, '.csv');
            $cityList[$cityName] = $cityKana[$cityName];
        }
        // 月リスト取得
        foreach(range(1,12) as $i){
            $monthList[$i] = $i . "月";
        }
        // 移動平均期間
        foreach(range(1,20) as $i){
            $period[$i] = $i . "期間";
        }
        $this->set(compact('cityList', 'monthList', 'period'));

        // 選択場所の気温情報取得
        $city = $this->request->query('city');
        $month = $this->request->query('month');
        $runningMeanPeriod = !empty($this->request->query('runningMeanPeriod')) ? $this->request->query('runningMeanPeriod') : 0;
        exec("python3.8 " . PYTHON_SCRIPT . "displayMonthData.py {$city} {$month} {$runningMeanPeriod}", $output);
        $data=[];
        if(!empty($output)) {
            $data['image'] = $output[0];
            $data['city'] = $cityKana[$city];
        }
        $this->set(compact('data'));
    }
}