<div class="container">
<div class="container-fluid">
<div class="row main">
<div class="col-md-12">
<?= $this->Flash->render("auth") ?>
<?= $this->Flash->render() ?>
<?= $this->fetch('content') ?>
</div>
</div>
</div>
</div>