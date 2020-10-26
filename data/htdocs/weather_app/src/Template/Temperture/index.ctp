<h2>気温データ</h2>
<p>
<?php $city = $this->request->query('city'); ?>
<?= $this->Form->create('displayTerm', ['type' => 'get']); ?>
<?= $this->Form->input('city', ['type' => 'select', 'options' => $cityList, 'default' => $this->request->query('city')]); ?>
<?= $this->Form->input('month', ['type' => 'select', 'options' => array_combine(range(1, 12), range(1, 12)), 'default' => $this->request->query('month')]); ?>
<?= $this->Form->input('runningMeanPeriod', ['type' => 'select', 'options' => array_combine(range(1, 20), range(1, 20)), 'empty' => '選択しない', 'default' => $this->request->query('runningMeanPeriod')]); ?>
<?= $this->Form->submit('表示'); ?>
<?= $this->Form->end(); ?>
</p>
<div>都市:　<?= $data['city']; ?></div>
<?= $this->HTML->image($data['image']); ?>