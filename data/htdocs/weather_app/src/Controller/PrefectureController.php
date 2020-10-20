<?php
namespace App\Controller;
use App\Controller\AppController;

class PrefectureController extends AppController {
    public function initialize() {
        parent::initialize();
    }

    public function index() {
        // 選択場所リスト取得
        $dirList = glob(PYTHON_DATA_TEMP . '*');
        foreach($dirList as $dir) {
            $placeList[] = basename($dir, '.csv');
        }
        $this->set(compact('placeList'));

        // 選択場所の気温情報取得
        $place = $this->request->query('place');
        $month = $this->request->query('month');
        exec("python3.8 " . PYTHON_SCRIPT . "displayMonthData.py {$place} {$month}", $output);
        $data=[];
        if(!empty($output)) {
            $data['image'] = $output[0];
            $data['place'] = $place;
        }
        $this->set(compact('data'));
    }
}