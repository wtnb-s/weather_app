<h2>気温データ</h2>

<?= $this->Form->create('displayTerm', ['type' => 'get']); ?>
<table class="table">
<tbody>
<tr>
<th>都市</th>
<td>
<?= $this->Form->input('city',
  ['type' => 'select',
  'options' => $cityList,
  'default' => $this->request->query('city'),
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
<th>移動平均期間</th>
<td>
<?= $this->Form->input('runningMeanPeriod',
  ['label' => '移動平均期間',
   'type' => 'select',
   'options' => $period,
   'empty' => '選択しない',
   'default' => $this->request->query('runningMeanPeriod'),
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

<?= $this->HTML->image($data['image']); ?>