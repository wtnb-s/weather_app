<?php
namespace App\Model\Table;

use Cake\ORM\Query;
use Cake\ORM\Table;
use Cake\Utility\Text;
use Cake\Validation\Validator;

class CityTable extends Table {
    public function initialize(array $config) {
        parent::initialize($config);
    }

    public function getList() {
        $query = $this->find('all');
        $data = $query->toArray();
        return $data;
    }
}