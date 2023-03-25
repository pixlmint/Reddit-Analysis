CREATE database if not exists `reddit_analysis`;

USE `reddit_analysis`;

CREATE TABLE if not exists `post` (
  `id` int(11) NOT NULL,
  `id_post` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `date_posted` datetime NOT NULL,
  `id_subreddit` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE if not exists `posthistoryelement` (
  `id` int(11) NOT NULL,
  `date_saved` datetime NOT NULL,
  `score` int(11) NOT NULL,
  `num_comms` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE if not exists `subreddit` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO `subreddit` (`id`, `name`) VALUES
(1, 'dankmemes'),
(2, 'askreddit');

ALTER TABLE `post`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `posthistoryelement`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `subreddit`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `posthistoryelement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `subreddit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;
COMMIT;
