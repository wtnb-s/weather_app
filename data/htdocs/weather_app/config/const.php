<?php
use Cake\Core\Configure;

return [
    Configure::write([
        'variableList' => ['Precip' =>'降水量', 'Temp'=>'平均気温', 'MaxTemp'=>'最高気温', 'MinTemp'=>'最低気温', 'DailyRange' => '日較差']
    ])
];