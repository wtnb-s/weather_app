<h2>気象データ</h2>

<?= $this->Form->create('displayTerm', ['type' => 'get']); ?>
<table class="table">
<tbody>
<tr>
<th>年</th>
<td>
<?= $this->Form->input('year',
  ['type' => 'select',
  'options' => $yearList,
  'default' => $this->request->query('year'),
  'label' => false
 ]); ?>
</td>
<th>月</th>
<td>
<?= $this->Form->input('month', 
  ['type' => 'select',
  'options' => $monthList,
  'default' => $this->request->query('month'),
  'label' => false
  ]); ?>
</td>
<th>表示要素</th>
<td>
<?= $this->Form->input('variable', 
  ['type' => 'select',
  'options' => $variableList,
  'default' => $this->request->query('variable'),
  'label' => false
  ]); ?>
</td>
</tr>
</tbody>
</table>

<div class="display-submit">
<?= $this->Form->submit('表示', ['class' => "btn btn-submit"]); ?>
</div>
<?= $this->Form->end(); ?>

<div class="display-figure">
<p><?= $this->HTML->image($data['image'], ['alt' => 'map', 'usemap' => '#distributionMap']); ?></p>
<map name="distributionMap">
<?php foreach ($cityList as $city): ?>
    <area target="_blank" alt="<?= $city['city_alpha']?>" title="<?= $city['city_name']?>" href="http://localhost:18765/Location/index?city=<?= $city['city_alpha']?>&month=<?= $data['month']?>&variable=<?= $data['variable']?>&runningMeanPeriod=5" coords="<?= $city['x_label']?>, <?= $city['y_label']?>, 8" shape="circle">
<?php endforeach; ?>
</map>
</div>