<?php
namespace App\Controller;
use App\Controller\AppController;

class TempertureController extends AppController {
    public function initialize() {
        parent::initialize();
    }

    public function index() {
        // 選択場所リスト取得
        $dirList = glob(PYTHON_DATA_TEMP . '*');
        foreach($dirList as $dir) {
            $cityName = basename($dir, '.csv');
            $cityList[$cityName] = $cityName;
        }
        $this->set(compact('cityList'));

        // 選択場所の気温情報取得
        $city = $this->request->query('city');
        $month = $this->request->query('month');
        $runningMeanPeriod = !empty($this->request->query('runningMeanPeriod')) ? $this->request->query('runningMeanPeriod') : 0;
        exec("python3.8 " . PYTHON_SCRIPT . "displayMonthData.py {$city} {$month} {$runningMeanPeriod}", $output);
        $data=[];
        if(!empty($output)) {
            $data['image'] = $output[0];
            $data['city'] = $city;
        }
        $this->set(compact('data'));
    }
}