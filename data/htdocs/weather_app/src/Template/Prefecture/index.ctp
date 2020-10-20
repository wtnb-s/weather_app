<?php foreach($placeList as $place): ?>
    <div><a href="?place=<?= $place; ?>" ><?= $place; ?></a></div>
<?php endforeach; ?>

<div><?= $this->HTML->image($data['image']); ?></div>
<div>place:<?= $data['place']; ?></div>