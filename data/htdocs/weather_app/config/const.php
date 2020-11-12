<?php
use Cake\Core\Configure;

return [
    Configure::write([
        'variableList' => ['LLP'=>'地上気圧', 'SLP'=>'海面更生気圧', 'Precip' =>'降水量', 'Temp'=>'平均気温', 'MaxTemp'=>'最高気温', 'MinTemp'=>'最低気温', 'Humidity' => '湿度','Wind' => '風速', 'Daylight' => '日照時間', 'Snowfall' => '降雪量']
    ])
];