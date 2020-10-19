<?php
namespace App\Controller;
use App\Controller\AppController;

class PrefectureController extends AppController {
    public function initialize() {
        parent::initialize();
    }
    public function index() {
        // 選択する場所リスト取得

        // 選択した場所の気温情報取得
        $place = $this->request->query('place');
        exec("python3.8 " . PYTHON_SCRIPT . "displayMonthData.py {$place}", $output);
        $data=[];
        if(!empty($output)) {
            $data['image'] = $output[0];
            $data['place'] = $place;
        }

        $this->set(compact('data'));
    }
}