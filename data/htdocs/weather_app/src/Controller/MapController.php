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

        // 引数設定
        $data['fromYear'] = $this->request->query('fromYear');
        $data['toYear'] = $this->request->query('toYear');
        $data['month'] = $this->request->query('month');
        $data['variable'] = $this->request->query('variable');
        $data['analysisType'] = $this->request->query('analysisType');
    
        exec("python3.8 " . PYTHON_SCRIPT . "displayPlotMap.py {$data['fromYear']} {$data['toYear']} {$data['month']} {$data['variable']} {$data['analysisType']}", $output);

        if (!empty($output)) {
            $data['image'] = $output[0];
        }
        $this->set(compact('data'));
    }
}