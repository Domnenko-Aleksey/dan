--
--`components`
--
CREATE TABLE IF NOT EXISTS `component` (
`id` int(10) unsigned NOT NULL,
  `component` varchar(255) NOT NULL,
  `url` varchar(50) NOT NULL,
  `name` varchar(255) NOT NULL,
  `settings` text NOT NULL,
  `ordering` int NOT NULL
) AUTO_INCREMENT=1;

ALTER TABLE `component`
 ADD PRIMARY KEY (`id`), ADD KEY `url` (`url`);

ALTER TABLE `component`
MODIFY `id` int(10) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=1;


--
--`sections`
--
CREATE TABLE `sections` (
  `id` int(10) UNSIGNED NOT NULL,
  `catalog_id` int(10) UNSIGNED NOT NULL,
  `parent_id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(50) NOT NULL,
  `text` longtext NOT NULL,
  `data` text NOT NULL,
  `date` datetime NOT NULL,
  `status` int(3) NOT NULL,
  `ordering` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `sections`
  ADD PRIMARY KEY (`id`),
  ADD KEY `catalog_id` (`catalog_id`);

ALTER TABLE `sections`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;




CREATE TABLE `items` (
  `id` int(10) UNSIGNED NOT NULL,
  `section_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `text` longtext NOT NULL,
  `data` longtext NOT NULL,
  `date` datetime NOT NULL,
  `status` int(11) NOT NULL,
  `ordering` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

ALTER TABLE `items`
  ADD PRIMARY KEY (`id`),
  ADD KEY `section_id` (`section_id`);

ALTER TABLE `items`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
COMMIT;
