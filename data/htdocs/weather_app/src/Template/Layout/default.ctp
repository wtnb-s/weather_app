<?php
/**
 * CakePHP(tm) : Rapid Development Framework (https://cakephp.org)
 * Copyright (c) Cake Software Foundation, Inc. (https://cakefoundation.org)
 *
 * Licensed under The MIT License
 * For full copyright and license information, please see the LICENSE.txt
 * Redistributions of files must retain the above copyright notice.
 *
 * @copyright     Copyright (c) Cake Software Foundation, Inc. (https://cakefoundation.org)
 * @link          https://cakephp.org CakePHP(tm) Project
 * @since         0.10.0
 * @license       https://opensource.org/licenses/mit-license.php MIT License
 * @var \App\View\AppView $this
 */

$cakeDescription = 'CakePHP: the rapid development php framework';
?>
<!DOCTYPE html>
<html>
<head>
<?= $this->Html->charset() ?>
<?= $this->Html->meta('icon') ?>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>
<?= $cakeDescription ?>:
<?= $this->fetch('title') ?>
</title>
<!-- Bootstrap CSS -->
<?= $this->Html->css('bootstrap.min.css') ?>
<!-- Original CSS -->
<?= $this->Html->css('style.css') ?>
    
<?= $this->fetch('meta') ?>
<?= $this->fetch('css') ?>
<?= $this->fetch('script') ?>
</head>
<body>
<?= $this->element("content") ?>
<?= $this->Html->script('jquery-3.5.1.min.js') ?>
<?= $this->Html->script('bootstrap.min.js') ?>
</body>
</html>
