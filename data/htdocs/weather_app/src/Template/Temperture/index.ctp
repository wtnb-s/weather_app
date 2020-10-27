<h3>気温データ</h3>
<p>
<?= $this->Form->create('displayTerm', ['type' => 'get']); ?>
<?= $this->Form->input('city', ['label' => '都市', 'type' => 'select', 'options' => $cityList, 'default' => $this->request->query('city')]); ?>
<?= $this->Form->input('month', ['label' => '月', 'type' => 'select', 'options' => $monthList, 'default' => $this->request->query('month')]); ?>
<?= $this->Form->input('runningMeanPeriod', ['label' => '移動平均期間', 'type' => 'select', 'options' => $period, 'empty' => '選択しない', 'default' => $this->request->query('runningMeanPeriod')]); ?>
<?= $this->Form->submit('表示'); ?>
<?= $this->Form->end(); ?>
</p>

<?= $this->HTML->image($data['image']); ?>
