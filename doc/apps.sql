/*
 Navicat Premium Data Transfer

 Source Server         : noprom.docker
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : localhost
 Source Database       : nuts

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : utf-8

 Date: 10/26/2016 17:04:27 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `apps`
-- ----------------------------
DROP TABLE IF EXISTS `apps`;
CREATE TABLE `apps` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '主键',
  `url_md5` varchar(32) NOT NULL COMMENT '爬虫链接md5值',
  `url` varchar(255) NOT NULL COMMENT '爬虫链接',
  `pkg` varchar(200) NOT NULL COMMENT '包名',
  `lang` varchar(20) NOT NULL COMMENT '语言',
  `icon` varchar(500) NOT NULL COMMENT '图标地址',
  `data` text NOT NULL COMMENT '包详细信息, json格式',
  `create_time` int(13) unsigned NOT NULL COMMENT '创建时间戳',
  `update_time` int(13) unsigned NOT NULL COMMENT '更新时间戳',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

SET FOREIGN_KEY_CHECKS = 1;
