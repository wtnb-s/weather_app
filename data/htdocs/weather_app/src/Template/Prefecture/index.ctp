<h2>気温データ</h2>
<p>
<?= $this->Form->create('displayTerm', ['type' => 'get']); ?>
<?= $this->Form->input('place', ['type' => 'select', 'options' => $placeList]); ?>
<?= $this->Form->input('month', ['type' => 'select', 'options' => range(1, 12)]); ?>
<?= $this->Form->input('runningMeanPeriod', ['type' => 'select', 'options' => range(1, 20), 'empty' => '選択しない']); ?>
<?= $this->Form->submit('表示'); ?>
<?= $this->Form->end(); ?>
</p>
<div>地域:　<?= $data['place']; ?></div>
<div><?= $this->HTML->image($data['image']); ?></div>