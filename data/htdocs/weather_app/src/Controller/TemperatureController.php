<?php
namespace App\Controller;
use App\Controller\AppController;
use Cake\Core\Configure;
use Cake\Utility\Hash;

class TemperatureController extends AppController {
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

        // 引数設定
        $city = $this->request->query('city');
        $month = $this->request->query('month');
        $variable = $this->request->query('variable');
        $runningMeanPeriod = !empty($this->request->query('runningMeanPeriod')) ? $this->request->query('runningMeanPeriod') : 0;
    
        exec("python3.8 " . PYTHON_SCRIPT . "displayMonthWeather.py {$city} {$month} {$variable} {$runningMeanPeriod}", $output);

        $data=[];
        if (!empty($output)) {
            $data['image'] = $output[0];
            $data['city'] = $cityList[$city];
        }
        $this->set(compact('data'));
    }
}