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
        foreach (range(1901,2020) as $i){
            $yearList[$i] = $i . "年";
        }
        // 月リスト取得
        foreach (range(1,12) as $i){
            $monthList[$i] = $i . "月";
        }
        // 表示要素リスト取得
        $variableList = Configure::read('variableList');

        $this->set(compact('yearList', 'monthList', 'variableList'));

        // 引数設定
        $year = $this->request->query('year');
        $month = $this->request->query('month');
        $variable = $this->request->query('variable');
    
        exec("python3.8 " . PYTHON_SCRIPT . "displayPlotMap.py {$year} {$month} {$variable}", $output);

        $data=[];
        if (!empty($output)) {
            $data['image'] = $output[0];
        }
        $this->set(compact('data'));
    }
}