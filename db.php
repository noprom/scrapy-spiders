<?php
	
	phpinfo();die;
	$db_host = 'localhost';
	$db_user = 'root';
	$db_pwd = '1q2w3e4r5t';
	$db_name = 'nuts';
	$db_table = 'apps';

	$data = '/Users/noprom/Documents/Dev/Python/Pro/scrapy-spiders/gp-apps.json';

	$file = fopen($data, 'r');
	while ($line = fgets($file, 4096)) {
		$json = json_decode($line, true);
		var_dump($json);
	}
	fclose($file);

	$conn = mysql_connect($db_host, $db_user, $db_pwd);
	$sql = 'SELECT * FROM apps';
	$result = mysql_db_query($db_name, $sql, $conn);
	$row = mysql_fetch_array($result);