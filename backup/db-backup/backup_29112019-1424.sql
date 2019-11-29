-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Erstellungszeit: 29. Nov 2019 um 14:24
-- Server-Version: 10.4.6-MariaDB
-- PHP-Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `reddit_analysis`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `post`
--

CREATE TABLE `post` (
  `id` int(11) NOT NULL,
  `id_post` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `date_posted` datetime NOT NULL,
  `id_subreddit` int(11) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `post`
--

INSERT INTO `post` (`id`, `id_post`, `url`, `date_posted`, `id_subreddit`, `title`) VALUES
(1, 'e3e3ky', 'https://i.redd.it/t1r81qcybm141.jpg', '2019-11-29 21:23:33', 1, 'wait a minute'),
(2, 'e3e3fa', 'https://i.redd.it/n3u0pmvubm141.jpg', '2019-11-29 21:23:02', 1, 'Oh ok sure'),
(3, 'e3e3dk', 'https://i.redd.it/jn0ryojtbm141.png', '2019-11-29 21:22:51', 1, 'I am taking a business course'),
(4, 'e3e383', 'https://i.redd.it/ifdas97rbm141.jpg', '2019-11-29 21:22:28', 1, 'You ain\'t gonna do about it'),
(5, 'e3e378', 'https://i.imgur.com/rZm66ed.jpg', '2019-11-29 21:22:25', 1, 'Big brain time'),
(6, 'e3e2lc', 'https://i.redd.it/twg55cmgbm141.png', '2019-11-29 21:20:48', 1, 'We didn\'t talk about politics!'),
(7, 'e3e28f', 'https://i.redd.it/aua9yt0bbm141.jpg', '2019-11-29 21:19:57', 1, 'Just a normal day'),
(8, 'e3e26p', 'https://i.redd.it/iaoyvzv9bm141.jpg', '2019-11-29 21:19:44', 1, 'I hope they never find mine (credit to hbomb18181)'),
(9, 'e3e1ih', 'https://i.redd.it/6a616l2xam141.png', '2019-11-29 21:17:50', 1, 'Its so realistic'),
(10, 'e3e179', 'https://i.redd.it/wp4mhp7sam141.jpg', '2019-11-29 21:16:59', 1, 'His name was Rodrigo :('),
(11, 'e3e48n', 'https://www.reddit.com/r/AskReddit/comments/e3e48n/what_are_some_unexpected_benefits_of_living_below/', '2019-11-29 21:25:36', 2, 'What are some unexpected benefits of living below your means?'),
(12, 'e3e46z', 'https://www.reddit.com/r/AskReddit/comments/e3e46z/whats_your_strategy_for_hitting_on_a_woman_in_a/', '2019-11-29 21:25:28', 2, 'What\'s your strategy for hitting on a woman in a dark parking garage?'),
(13, 'e3e443', 'https://www.reddit.com/r/AskReddit/comments/e3e443/whats_your_favorite_plant_in_stardew_valley/', '2019-11-29 21:25:17', 2, 'What\'s your favorite plant in Stardew Valley?'),
(14, 'e3e437', 'https://www.reddit.com/r/AskReddit/comments/e3e437/what_post_or_comment_got_you_gold/', '2019-11-29 21:25:14', 2, 'What post or comment got you gold?'),
(15, 'e3e407', 'https://www.reddit.com/r/AskReddit/comments/e3e407/today_is_your_birthday_what_important_lesson_did/', '2019-11-29 21:24:57', 2, 'Today is your birthday, What important lesson did you learn that you didn\'t know a year ago?'),
(16, 'e3dtpc', 'https://www.reddit.com/r/AskReddit/comments/e3dtpc/dear_redditors_what_is_a_rule_you_follow_which/', '2019-11-29 20:54:43', 2, 'Dear redditors, what is a rule you follow which doesn\'t exist?'),
(17, 'e3e3vf', 'https://www.reddit.com/r/AskReddit/comments/e3e3vf/where_is_a_good_destination_for_a_three_day_solo/', '2019-11-29 21:24:30', 2, 'Where is a good destination for a three day solo getaway?'),
(18, 'e3e3r1', 'https://www.reddit.com/r/AskReddit/comments/e3e3r1/what_did_you_always_want_to_learn_but_you_were/', '2019-11-29 21:24:06', 2, 'What did you always want to learn but you were too lazy to look up?'),
(19, 'e3e3qd', 'https://www.reddit.com/r/AskReddit/comments/e3e3qd/what_is_one_thing_in_life_except_death_that_is/', '2019-11-29 21:24:02', 2, 'What is one thing in life (except death) that is guaranteed?'),
(20, 'e3e3pu', 'https://www.reddit.com/r/AskReddit/comments/e3e3pu/what_would_you_do_if_you_had_the_ability_to_flip/', '2019-11-29 21:23:59', 2, 'What would you do if you had the ability to flip gravity on any object, but only one at a time?'),
(21, 'e3e4e8', 'https://i.redd.it/id8ub66dcm141.jpg', '2019-11-29 21:26:10', 1, 'Taxes in a nutshell'),
(22, 'e3e4in', 'https://www.reddit.com/r/AskReddit/comments/e3e4in/would_you_change_your_gender_why/', '2019-11-29 21:26:32', 2, 'Would you change your gender? Why?'),
(23, 'e3e4eb', 'https://www.reddit.com/r/AskReddit/comments/e3e4eb/what_is_the_most_morbidly_beautiful_thingevent/', '2019-11-29 21:26:10', 2, 'What is the most morbidly beautiful thing/event you have witnessed?'),
(24, 'e3e4x9', 'https://i.redd.it/e3z70exocm141.jpg', '2019-11-29 21:27:43', 1, 'Hell yeah'),
(25, 'e3e4yz', 'https://www.reddit.com/r/AskReddit/comments/e3e4yz/the_answer_is_2_and_a_half_what_was_the_question/', '2019-11-29 21:27:51', 2, 'The answer is 2 and a half. What was the question?'),
(26, 'e3e4y6', 'https://www.reddit.com/r/AskReddit/comments/e3e4y6/what_is_the_difference_between_commitment_and/', '2019-11-29 21:27:47', 2, 'What is the difference between commitment and loyalty?'),
(27, 'e3e4vh', 'https://www.reddit.com/r/AskReddit/comments/e3e4vh/2019_is_almost_done_and_its_holiday_season_what/', '2019-11-29 21:27:34', 2, '2019 is almost done and it\'s holiday season! What are some things that happened to you this year that made you happy?'),
(28, 'e3e4pa', 'https://www.reddit.com/r/AskReddit/comments/e3e4pa/hi_redditors_how_is_your_school_schedule/', '2019-11-29 21:27:06', 2, 'Hi redditors, how is your school schedule?'),
(29, 'e3e4o7', 'https://www.reddit.com/r/AskReddit/comments/e3e4o7/the_year_is_2020_and_aliens_have_declared_war_on/', '2019-11-29 21:26:59', 2, 'The year is 2020 and aliens have declared war on Earth. With only $1B at your disposal, how do you effectively fight them off?'),
(30, 'e3e5e5', 'https://i.redd.it/lci27yjncm141.png', '2019-11-29 21:29:07', 1, 'lol i dunno how'),
(31, 'e3e5ei', 'https://www.reddit.com/r/AskReddit/comments/e3e5ei/any_subreddits_for_tips_for_people_who_cant_stand/', '2019-11-29 21:29:09', 2, 'Any subreddits for tips for people who can’t stand the cold and are moving to a place like Alaska or Wisconsin?'),
(32, 'e3e5eg', 'https://www.reddit.com/r/AskReddit/comments/e3e5eg/what_do_you_wish_people_were_more_mindful_about/', '2019-11-29 21:29:09', 2, 'What do you wish people were more mindful about?'),
(33, 'e3e5cc', 'https://www.reddit.com/r/AskReddit/comments/e3e5cc/what_is_your_favorite_smell/', '2019-11-29 21:28:58', 2, 'What is your favorite smell?'),
(34, 'e3e5bh', 'https://www.reddit.com/r/AskReddit/comments/e3e5bh/what_age_did_you_hit_your_physical_peak/', '2019-11-29 21:28:51', 2, 'What age did you hit your physical peak?'),
(35, 'e3e5am', 'https://www.reddit.com/r/AskReddit/comments/e3e5am/what_will_be_invented_in_the_2020s/', '2019-11-29 21:28:46', 2, 'What will be invented in the 2020s?'),
(36, 'e3e5a6', 'https://www.reddit.com/r/AskReddit/comments/e3e5a6/those_who_took_part_in_don_trump_jrs_triggered/', '2019-11-29 21:28:44', 2, 'Those who took part in Don Trump Jr.\'s \"Triggered\" challenge, WHY?'),
(37, 'e3e59x', 'https://www.reddit.com/r/AskReddit/comments/e3e59x/if_youre_being_honest_how_long_would_you_survive/', '2019-11-29 21:28:42', 2, 'If you\'re being honest, how long would you survive during the zombie apocalypse and what\'s your plan?'),
(38, 'e3e58v', 'https://www.reddit.com/r/AskReddit/comments/e3e58v/you_die_and_become_a_ghost_u_can_choose_2/', '2019-11-29 21:28:36', 2, 'You die and become a ghost. U can choose 2 abilities. Teleportation, moving objects and whispering to humans, flight, moving through walls, interacting with the ghost world. Which do you choose and why ?'),
(39, 'e3e6wk', 'https://i.redd.it/y4pc30indm141.png', '2019-11-29 21:33:54', 1, 'smells like gay'),
(40, 'e3e6t0', 'https://i.redd.it/4u7c9pmqdm141.jpg', '2019-11-29 21:33:34', 1, 'Sad T-Series noises'),
(41, 'e3e6f3', 'https://i.redd.it/w086z0midm141.jpg', '2019-11-29 21:32:19', 1, 'Technically true'),
(42, 'e3e5pz', 'https://i.redd.it/86n3z2v3dm141.jpg', '2019-11-29 21:30:03', 1, 'Gotta celebrate fellas'),
(43, 'e3e5p9', 'https://i.redd.it/6y4bpjm3dm141.png', '2019-11-29 21:29:59', 1, 'Uncle Iroh was truly one of a kind'),
(44, 'e3e7bw', 'https://www.reddit.com/r/AskReddit/comments/e3e7bw/those_who_are_65_or_older_and_still_working_why/', '2019-11-29 21:35:06', 2, 'Those who are 65 or older and still working, why haven\'t you retired yet?'),
(45, 'e3e79d', 'https://www.reddit.com/r/AskReddit/comments/e3e79d/what_side_dishes_did_you_have_at_thanksgiving/', '2019-11-29 21:34:52', 2, 'What side dishes did you have at Thanksgiving?'),
(46, 'e3e789', 'https://www.reddit.com/r/AskReddit/comments/e3e789/what_is_the_one_story_or_stories_that_you_will/', '2019-11-29 21:34:47', 2, 'What is the one story, or stories, that you will always remember with clarity, no matter how many years pass?'),
(47, 'e3e76a', 'https://www.reddit.com/r/AskReddit/comments/e3e76a/whats_your_take_on_misanthropy/', '2019-11-29 21:34:40', 2, 'What\'s your take on misanthropy?'),
(48, 'e3e74g', 'https://www.reddit.com/r/AskReddit/comments/e3e74g/what_is_something_you_anonymously_wish_to_tell/', '2019-11-29 21:34:30', 2, 'What is something you anonymously wish to tell someone but cannot for whatever reason?'),
(49, 'e3e73k', 'https://www.reddit.com/r/AskReddit/comments/e3e73k/what_is_weirdest_and_longest_name_you_heard/', '2019-11-29 21:34:24', 2, 'What is weirdest and longest name you heard?'),
(50, 'e3e72d', 'https://www.reddit.com/r/AskReddit/comments/e3e72d/whats_your_worst_second_hand_embarrassment_youve/', '2019-11-29 21:34:20', 2, 'What\'s your worst second hand embarrassment you\'ve experienced?'),
(51, 'e3e6lx', 'https://www.reddit.com/r/AskReddit/comments/e3e6lx/people_who_have_been_shot_what_was_it_like/', '2019-11-29 21:32:53', 2, 'People who have been shot, what was it like?'),
(52, 'e3e6l8', 'https://www.reddit.com/r/AskReddit/comments/e3e6l8/whats_the_best_black_friday_deal_youve_seen_so_far/', '2019-11-29 21:32:49', 2, 'What’s the best Black Friday deal you’ve seen so far?'),
(53, 'e3e6kx', 'https://www.reddit.com/r/AskReddit/comments/e3e6kx/how_would_you_like_to_die/', '2019-11-29 21:32:47', 2, 'How would you like to die?'),
(54, 'e3eaem', 'https://i.redd.it/a7f7uhblfm141.jpg', '2019-11-29 21:43:56', 1, 'It do be like that'),
(55, 'e3ea07', 'https://i.redd.it/a6k7am4dfm141.png', '2019-11-29 21:42:40', 1, 'Guys she\'s gone forever :('),
(56, 'e3e9vj', 'https://i.redd.it/jwfzijh7fm141.jpg', '2019-11-29 21:42:20', 1, 'Every single time'),
(57, 'e3e8w8', 'https://i.redd.it/94jqhbgsem141.jpg', '2019-11-29 21:39:27', 1, 'Me on December 1st'),
(58, 'e3eaxl', 'https://www.reddit.com/r/AskReddit/comments/e3eaxl/what_are_some_fun_redneck_exercisesworkouts_why/', '2019-11-29 21:45:28', 2, 'What are some fun redneck exercises/workouts? Why?'),
(59, 'e3eawl', 'https://www.reddit.com/r/AskReddit/comments/e3eawl/men_of_reddit_when_you_get_horny_do_you_just_want/', '2019-11-29 21:45:22', 2, 'Men of reddit. When you get horny, do you just want to fuck your girls senseless of do you like making sweet tender love? If both, which one is more common?'),
(60, 'e3eavu', 'https://www.reddit.com/r/AskReddit/comments/e3eavu/as_the_christmas_times_draw_near_what_are_some/', '2019-11-29 21:45:19', 2, 'As the Christmas times draw near, what are some interesting/wtf facts about Christmas?'),
(61, 'e3ear3', 'https://www.reddit.com/r/AskReddit/comments/e3ear3/which_tv_sitcom_would_you_star_in/', '2019-11-29 21:44:53', 2, 'Which TV sitcom would you star in?'),
(62, 'e3eao7', 'https://www.reddit.com/r/AskReddit/comments/e3eao7/how_would_you_describe_life/', '2019-11-29 21:44:40', 2, 'How would you describe life?'),
(63, 'e3eant', 'https://www.reddit.com/r/AskReddit/comments/e3eant/what_problem_did_you_solve_in_a_around_the/', '2019-11-29 21:44:39', 2, 'What problem did you solve in a \"Around the maginot\" style?'),
(64, 'e3eag4', 'https://www.reddit.com/r/AskReddit/comments/e3eag4/when_you_look_back_on_the_2010s_what_moment_of/', '2019-11-29 21:44:04', 2, 'When you look back on the 2010s, what moment of your life will stand out in your memory?'),
(65, 'e3eaby', 'https://www.reddit.com/r/AskReddit/comments/e3eaby/whats_the_weirdest_thing_thats_ever_happened_to/', '2019-11-29 21:43:42', 2, 'What\'s the weirdest thing that\'s ever happened to you during a Thanksgiving family gathering?'),
(66, 'e3eaag', 'https://www.reddit.com/r/AskReddit/comments/e3eaag/aliens_of_reddit_what_is_something_stupid_that/', '2019-11-29 21:43:35', 2, 'Aliens of Reddit, what is something stupid that you’ve seen a dumb human do?'),
(67, 'e3ea9f', 'https://www.reddit.com/r/AskReddit/comments/e3ea9f/what_is_your_best_approach_to_making_a_point_on/', '2019-11-29 21:43:30', 2, 'What is your best approach to making a point on the internet without being inflammatory?'),
(68, 'e3ec3j', 'https://i.redd.it/tu6dd5ehgm141.png', '2019-11-29 21:49:03', 1, 'Low quality swamp'),
(69, 'e3eayq', 'https://i.redd.it/8k3x5ypvfm141.jpg', '2019-11-29 21:45:34', 1, 'You get what you fucking deserve!'),
(70, 'e3ec31', 'https://www.reddit.com/r/AskReddit/comments/e3ec31/what_is_the_first_thing_you_would_do_with_a_taser/', '2019-11-29 21:49:00', 2, 'What is the first thing you would do with a taser?'),
(71, 'e3ec0k', 'https://www.reddit.com/r/AskReddit/comments/e3ec0k/if_you_could_go_back_in_time_to_change_one_thing/', '2019-11-29 21:48:45', 2, 'If you could go back in time to change one thing you have done in the past, what would you change?'),
(72, 'e3ebz1', 'https://www.reddit.com/r/AskReddit/comments/e3ebz1/people_who_went_to_their_10_year_graduation/', '2019-11-29 21:48:36', 2, 'People who went to their 10 year graduation reunion, what was the quiet kid like?'),
(73, 'e3ebyk', 'https://www.reddit.com/r/AskReddit/comments/e3ebyk/guys_of_reddit_do_you_like_making_the_first_move/', '2019-11-29 21:48:34', 2, 'Guys of reddit, do you like making the first move? Why/why not?'),
(74, 'e3ebyg', 'https://www.reddit.com/r/AskReddit/comments/e3ebyg/what_is_the_best_thing_to_do_in_the_case_that/', '2019-11-29 21:48:33', 2, 'What is the best thing to do in the case that your child/parent/sibling/SO/any other person close to you gets kidnapped and the kidnapper has warned you not to tell the police?'),
(75, 'e3ebxu', 'https://www.reddit.com/r/AskReddit/comments/e3ebxu/who_are_your_top_three_celebrities_that_best/', '2019-11-29 21:48:29', 2, 'Who are your top three celebrities that best define this decade?'),
(76, 'e3ebog', 'https://www.reddit.com/r/AskReddit/comments/e3ebog/what_was_the_weirdest_reason_the_characters_in_a/', '2019-11-29 21:47:48', 2, 'What was the weirdest reason the characters in a porn movie started having sex ?'),
(77, 'e3ebnq', 'https://www.reddit.com/r/AskReddit/comments/e3ebnq/girls_of_reddit_what_is_something_a_guy_should/', '2019-11-29 21:47:44', 2, 'Girls of reddit. What is something a guy should NOT do on a first date?'),
(78, 'e3eb7o', 'https://www.reddit.com/r/AskReddit/comments/e3eb7o/you_wake_up_in_a_forest_you_find_out_that_this_is/', '2019-11-29 21:46:23', 2, 'You wake up in a forest. You find out that this is earth in its natural state with many animals, trees, and rivers. As you walk around, you find another human. When she sees you, she says that she is tired and lonely. What will you do?'),
(79, 'e3eb7a', 'https://www.reddit.com/r/AskReddit/comments/e3eb7a/if_it_was_discovered_that_another_species/', '2019-11-29 21:46:20', 2, 'If it was discovered that another species developed human-like intelligence, how would humans react?'),
(80, 'e3ecdt', 'https://i.redd.it/ancdr0bngm141.jpg', '2019-11-29 21:49:51', 1, 'donkæ'),
(81, 'e3ec9v', 'https://i.redd.it/s4gl3qukgm141.jpg', '2019-11-29 21:49:29', 1, 'Paint the house white'),
(82, 'e3ecn2', 'https://www.reddit.com/r/AskReddit/comments/e3ecn2/redditors_with_straight_parents_what_was_your/', '2019-11-29 21:50:38', 2, 'Redditors with straight parents, what was your experience like?'),
(83, 'e3ecmx', 'https://www.reddit.com/r/AskReddit/comments/e3ecmx/how_stupid_are_you/', '2019-11-29 21:50:37', 2, 'How stupid are you?'),
(84, 'e3ecm8', 'https://www.reddit.com/r/AskReddit/comments/e3ecm8/what_was_the_bestworst_update_in_reddit_history/', '2019-11-29 21:50:35', 2, 'What was the best/worst update in reddit history?'),
(85, 'e3ecfb', 'https://www.reddit.com/r/AskReddit/comments/e3ecfb/for_everyone_who_got_everything_they_wanted_in/', '2019-11-29 21:50:00', 2, 'For everyone who got everything they wanted in life, how do/did you feel? Was there hapiness in the end? Feeling of emptiness, like you feel after feeling finishing a good video game or a book? Or did you just move on to the next thing without much though'),
(86, 'e3ece8', 'https://www.reddit.com/r/AskReddit/comments/e3ece8/girls_of_reddit_what_would_you_do_if_a_boy_asked/', '2019-11-29 21:49:54', 2, 'Girls of Reddit, what would you do if a boy asked to eat with you?'),
(87, 'e3ec94', 'https://www.reddit.com/r/AskReddit/comments/e3ec94/whats_the_worst_kind_of_gift_to_wrap_and_what/', '2019-11-29 21:49:26', 2, 'What\'s the worst kind of gift to wrap and what tips can you give on wrapping it properly?'),
(88, 'e3ecx7', 'https://i.redd.it/rdwldijwgm141.jpg', '2019-11-29 21:51:17', 1, 'bing bong bang hehe'),
(89, 'e3ecu4', 'https://i.redd.it/0k3iqihvgm141.jpg', '2019-11-29 21:51:08', 1, '100% pure shit'),
(90, 'e3ed0p', 'https://www.reddit.com/r/AskReddit/comments/e3ed0p/what_are_some_jobs_or_business_best_for_an/', '2019-11-29 21:51:29', 2, 'What are some jobs or business best for an introvert ?'),
(91, 'e3ecw7', 'https://www.reddit.com/r/AskReddit/comments/e3ecw7/have_you_ever_woke_up_in_the_middle_of_a_dream/', '2019-11-29 21:51:15', 2, 'Have you ever woke up in the middle of a dream and the dream was so interesting that you wanted to go back to sleep to see the end of it? If so, what was the dream?'),
(92, 'e3edkl', 'https://www.reddit.com/r/AskReddit/comments/e3edkl/what_is_the_one_gold_or_higher_award_for_a/', '2019-11-29 21:53:07', 2, 'What is the one gold (or higher) award for a comment that you got that you\'re proud of?'),
(93, 'e3edi4', 'https://www.reddit.com/r/AskReddit/comments/e3edi4/if_isis_had_a_application_form_what_would_the/', '2019-11-29 21:52:53', 2, 'If ISIS had a application form, what would the questions be?'),
(94, 'e3edhy', 'https://www.reddit.com/r/AskReddit/comments/e3edhy/which_character_would_you_be_if_you_were_in_that/', '2019-11-29 21:52:52', 2, 'Which character would you be if you were in that sitcom?'),
(95, 'e3edhl', 'https://www.reddit.com/r/AskReddit/comments/e3edhl/nonamericans_of_reddit_what_would_be_considered/', '2019-11-29 21:52:51', 2, 'Non-Americans of Reddit, What would be considered the Bigfoot or Area 51 equivalent of your country?'),
(96, 'e3edh0', 'https://www.reddit.com/r/AskReddit/comments/e3edh0/what_are_some_good_crime_related_movies/', '2019-11-29 21:52:48', 2, 'What are some good crime related movies?'),
(97, 'e3edfd', 'https://www.reddit.com/r/AskReddit/comments/e3edfd/what_happens_to_the_body_if_someone_dies_in/', '2019-11-29 21:52:38', 2, 'What happens to the body if someone dies in hospital or at home?'),
(98, 'e3edct', 'https://www.reddit.com/r/AskReddit/comments/e3edct/do_you_think_white_men_deserve_more/', '2019-11-29 21:52:25', 2, 'Do you think white men deserve more representation in Japanese porn? Why or why not?'),
(99, 'e3edch', 'https://www.reddit.com/r/AskReddit/comments/e3edch/serious_what_are_some_subreddits_that_at_a_first/', '2019-11-29 21:52:24', 2, '[Serious] What are some subreddits that at a first glance look bad, but are actually innocent or even wholesome?'),
(100, 'e3el6n', 'https://i.redd.it/ahotc2aykm141.jpg', '2019-11-29 22:13:58', 1, 'Reality is often disappointing'),
(101, 'e3ekze', 'https://i.redd.it/moo9fi8ukm141.jpg', '2019-11-29 22:13:21', 1, 'guys please call my work tonight'),
(102, 'e3emny', 'https://i.imgur.com/I2Z1lI5.jpg', '2019-11-29 22:18:04', 1, 'mods are gayer than Tom Cruise'),
(103, 'e3elyl', 'https://i.redd.it/t47u0zeblm141.png', '2019-11-29 22:16:07', 1, 'Don\'t do it'),
(104, 'e3elwl', 'https://i.redd.it/dce76nualm141.jpg', '2019-11-29 22:15:59', 1, 'Even the like/dislike ratio agree'),
(105, 'e3ekm8', 'https://i.redd.it/unhncuokkm141.png', '2019-11-29 22:12:16', 1, 'Only scientists will understand this'),
(106, 'e3ekg7', 'https://i.redd.it/q6zrs74gkm141.jpg', '2019-11-29 22:11:47', 1, 'It would filter out normies'),
(107, 'e3ek25', 'https://i.redd.it/fb6kn47dkm141.jpg', '2019-11-29 22:10:44', 1, 'Joker memes r da best'),
(108, 'e3ejwm', 'https://i.redd.it/9qb78y7bkm141.jpg', '2019-11-29 22:10:23', 1, 'Not if you have no dad'),
(109, 'e3ej90', 'https://i.redd.it/3spc7zuzjm141.jpg', '2019-11-29 22:08:38', 1, 'I thought it was a documentary on National Geographic'),
(110, 'e3en19', 'https://www.reddit.com/r/AskReddit/comments/e3en19/serious_people_who_were_on_the_dark_web_what/', '2019-11-29 22:19:08', 2, '(Serious) People who were on the dark web, what happened?'),
(111, 'e3emvh', 'https://www.reddit.com/r/AskReddit/comments/e3emvh/money_saved_is_money_earned_what_are_some_of_your/', '2019-11-29 22:18:37', 2, 'Money saved is money earned. What are some of your tried and tested money saving techniques?'),
(112, 'e3emv8', 'https://www.reddit.com/r/AskReddit/comments/e3emv8/whats_the_creepiest_thing_thats_ever_happened_to/', '2019-11-29 22:18:36', 2, 'What’s the creepiest thing that’s ever happened to you?'),
(113, 'e3emu6', 'https://www.reddit.com/r/AskReddit/comments/e3emu6/god_said_let_there_be_light_what_would_you_say/', '2019-11-29 22:18:33', 2, 'God said: let there be light! What would you say: let there be ...?'),
(114, 'e3emtv', 'https://www.reddit.com/r/AskReddit/comments/e3emtv/what_is_the_taste_of_water/', '2019-11-29 22:18:32', 2, 'What is the taste of water..?'),
(115, 'e3emta', 'https://www.reddit.com/r/AskReddit/comments/e3emta/who_believe_in_santa_claus/', '2019-11-29 22:18:30', 2, 'Who believe in Santa claus?'),
(116, 'e3ems9', 'https://www.reddit.com/r/AskReddit/comments/e3ems9/how_to_enjoy_life/', '2019-11-29 22:18:25', 2, 'How to Enjoy Life ?'),
(117, 'e3empc', 'https://www.reddit.com/r/AskReddit/comments/e3empc/if_you_could_change_just_a_single_moment_in_your/', '2019-11-29 22:18:13', 2, 'If you could change just a single moment in your life, what would it be and why?'),
(118, 'e3emoh', 'https://www.reddit.com/r/AskReddit/comments/e3emoh/what_important_thing_is_about_to_happen_and_noone/', '2019-11-29 22:18:08', 2, 'What important thing is about to happen and noone is aware about it?'),
(119, 'e3emmj', 'https://www.reddit.com/r/AskReddit/comments/e3emmj/how_should_we_stop_nazi_china/', '2019-11-29 22:17:57', 2, 'How should we stop Nazi China?'),
(120, 'e3eosm', 'https://i.imgur.com/tyQbw5z.jpg', '2019-11-29 22:23:44', 1, 'That’s not nice'),
(121, 'e3eon3', 'https://i.redd.it/zezs0kcmmm141.jpg', '2019-11-29 22:23:20', 1, 'Everytime a stronger one comes');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `posthistoryelement`
--

CREATE TABLE `posthistoryelement` (
  `id_post` int(11) NOT NULL,
  `id` int(11) NOT NULL,
  `date_saved` datetime NOT NULL,
  `score` int(11) NOT NULL,
  `num_comms` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `posthistoryelement`
--

INSERT INTO `posthistoryelement` (`id_post`, `id`, `date_saved`, `score`, `num_comms`) VALUES
(0, 1, '2019-11-29 13:25:34', 11, 0),
(0, 2, '2019-11-29 13:25:36', 13, 0),
(0, 3, '2019-11-29 13:25:37', 8, 0),
(0, 4, '2019-11-29 13:25:38', 7, 1),
(0, 5, '2019-11-29 13:25:40', 11, 0),
(0, 6, '2019-11-29 13:25:41', 17, 0),
(0, 7, '2019-11-29 13:25:42', 18, 1),
(0, 8, '2019-11-29 13:25:44', 18, 3),
(0, 9, '2019-11-29 13:25:45', 15, 0),
(0, 10, '2019-11-29 13:25:46', 19, 2),
(0, 11, '2019-11-29 13:25:48', 1, 0),
(0, 12, '2019-11-29 13:25:49', 1, 0),
(0, 13, '2019-11-29 13:25:51', 1, 0),
(0, 14, '2019-11-29 13:25:52', 1, 0),
(0, 15, '2019-11-29 13:25:53', 1, 0),
(0, 16, '2019-11-29 13:25:54', 1, 2),
(0, 17, '2019-11-29 13:25:56', 1, 1),
(0, 18, '2019-11-29 13:25:57', 2, 2),
(0, 19, '2019-11-29 13:25:58', 1, 4),
(0, 20, '2019-11-29 13:26:00', 1, 1),
(0, 21, '2019-11-29 13:26:31', 1, 0),
(0, 22, '2019-11-29 13:26:32', 17, 2),
(0, 23, '2019-11-29 13:26:34', 14, 1),
(0, 24, '2019-11-29 13:26:35', 11, 0),
(0, 25, '2019-11-29 13:26:36', 9, 1),
(0, 26, '2019-11-29 13:26:37', 11, 0),
(0, 27, '2019-11-29 13:26:38', 18, 0),
(0, 28, '2019-11-29 13:26:39', 20, 1),
(0, 29, '2019-11-29 13:26:41', 18, 5),
(0, 30, '2019-11-29 13:26:42', 16, 0),
(0, 31, '2019-11-29 13:26:44', 1, 0),
(0, 32, '2019-11-29 13:26:45', 1, 0),
(0, 33, '2019-11-29 13:26:46', 1, 1),
(0, 34, '2019-11-29 13:26:47', 0, 3),
(0, 35, '2019-11-29 13:26:49', 0, 1),
(0, 36, '2019-11-29 13:26:50', 1, 1),
(0, 37, '2019-11-29 13:26:51', 1, 2),
(0, 38, '2019-11-29 13:26:52', 2, 3),
(0, 39, '2019-11-29 13:26:54', 1, 4),
(0, 40, '2019-11-29 13:26:55', 2, 2),
(0, 41, '2019-11-29 13:28:26', 3, 0),
(0, 42, '2019-11-29 13:28:27', 10, 0),
(0, 43, '2019-11-29 13:28:28', 26, 4),
(0, 44, '2019-11-29 13:28:28', 22, 1),
(0, 45, '2019-11-29 13:28:29', 14, 1),
(0, 46, '2019-11-29 13:28:30', 10, 2),
(0, 47, '2019-11-29 13:28:31', 16, 0),
(0, 48, '2019-11-29 13:28:32', 23, 0),
(0, 49, '2019-11-29 13:28:33', 27, 1),
(0, 50, '2019-11-29 13:28:34', 18, 6),
(0, 51, '2019-11-29 13:28:35', 1, 0),
(0, 52, '2019-11-29 13:28:35', 1, 0),
(0, 53, '2019-11-29 13:28:36', 1, 0),
(0, 54, '2019-11-29 13:28:37', 0, 2),
(0, 55, '2019-11-29 13:28:38', 1, 2),
(0, 56, '2019-11-29 13:28:38', 2, 5),
(0, 57, '2019-11-29 13:28:39', 1, 0),
(0, 58, '2019-11-29 13:28:40', 1, 2),
(0, 59, '2019-11-29 13:28:41', 0, 5),
(0, 60, '2019-11-29 13:28:42', 1, 2),
(0, 61, '2019-11-29 13:29:12', 1, 0),
(0, 62, '2019-11-29 13:29:13', 3, 0),
(0, 63, '2019-11-29 13:29:14', 10, 0),
(0, 64, '2019-11-29 13:29:14', 27, 4),
(0, 65, '2019-11-29 13:29:15', 22, 1),
(0, 66, '2019-11-29 13:29:16', 14, 1),
(0, 67, '2019-11-29 13:29:16', 11, 2),
(0, 68, '2019-11-29 13:29:17', 16, 0),
(0, 69, '2019-11-29 13:29:17', 24, 0),
(0, 70, '2019-11-29 13:29:18', 28, 1),
(0, 71, '2019-11-29 13:29:19', 1, 0),
(0, 72, '2019-11-29 13:29:20', 1, 0),
(0, 73, '2019-11-29 13:29:20', 1, 0),
(0, 74, '2019-11-29 13:29:21', 2, 1),
(0, 75, '2019-11-29 13:29:21', 1, 0),
(0, 76, '2019-11-29 13:29:22', 1, 0),
(0, 77, '2019-11-29 13:29:23', 1, 0),
(0, 78, '2019-11-29 13:29:24', 1, 0),
(0, 79, '2019-11-29 13:29:24', 1, 4),
(0, 80, '2019-11-29 13:29:25', 1, 1),
(0, 81, '2019-11-29 13:35:14', 5, 0),
(0, 82, '2019-11-29 13:35:15', 10, 0),
(0, 83, '2019-11-29 13:35:16', 14, 0),
(0, 84, '2019-11-29 13:35:18', 27, 0),
(0, 85, '2019-11-29 13:35:19', 14, 1),
(0, 86, '2019-11-29 13:35:21', 12, 0),
(0, 87, '2019-11-29 13:35:22', 17, 0),
(0, 88, '2019-11-29 13:35:23', 28, 0),
(0, 89, '2019-11-29 13:35:25', 52, 7),
(0, 90, '2019-11-29 13:35:26', 31, 1),
(0, 91, '2019-11-29 13:35:28', 1, 0),
(0, 92, '2019-11-29 13:35:30', 1, 0),
(0, 93, '2019-11-29 13:35:31', 1, 0),
(0, 94, '2019-11-29 13:35:32', 1, 0),
(0, 95, '2019-11-29 13:35:34', 1, 0),
(0, 96, '2019-11-29 13:35:35', 0, 0),
(0, 97, '2019-11-29 13:35:36', 1, 0),
(0, 98, '2019-11-29 13:35:38', 0, 0),
(0, 99, '2019-11-29 13:35:39', 2, 5),
(0, 100, '2019-11-29 13:35:41', 2, 7),
(0, 101, '2019-11-29 13:45:20', 9, 0),
(0, 102, '2019-11-29 13:45:22', 12, 0),
(0, 103, '2019-11-29 13:45:23', 13, 0),
(0, 104, '2019-11-29 13:45:24', 20, 0),
(0, 105, '2019-11-29 13:45:26', 21, 1),
(0, 106, '2019-11-29 13:45:27', 36, 4),
(0, 107, '2019-11-29 13:45:29', 33, 1),
(0, 108, '2019-11-29 13:45:30', 63, 1),
(0, 109, '2019-11-29 13:45:32', 32, 2),
(0, 110, '2019-11-29 13:45:33', 22, 0),
(0, 111, '2019-11-29 13:45:35', 1, 0),
(0, 112, '2019-11-29 13:45:36', 1, 0),
(0, 113, '2019-11-29 13:45:38', 1, 0),
(0, 114, '2019-11-29 13:45:39', 1, 0),
(0, 115, '2019-11-29 13:45:40', 1, 1),
(0, 116, '2019-11-29 13:45:42', 1, 0),
(0, 117, '2019-11-29 13:45:43', 2, 0),
(0, 118, '2019-11-29 13:45:44', 1, 0),
(0, 119, '2019-11-29 13:45:46', 2, 4),
(0, 120, '2019-11-29 13:45:47', 2, 2),
(0, 121, '2019-11-29 13:49:05', 1, 0),
(0, 122, '2019-11-29 13:49:06', 14, 0),
(0, 123, '2019-11-29 13:49:07', 24, 1),
(0, 124, '2019-11-29 13:49:07', 18, 1),
(0, 125, '2019-11-29 13:49:08', 23, 0),
(0, 126, '2019-11-29 13:49:09', 25, 0),
(0, 127, '2019-11-29 13:49:09', 24, 1),
(0, 128, '2019-11-29 13:49:10', 42, 4),
(0, 129, '2019-11-29 13:49:11', 35, 1),
(0, 130, '2019-11-29 13:49:11', 75, 1),
(0, 131, '2019-11-29 13:49:12', 1, 0),
(0, 132, '2019-11-29 13:49:13', 1, 0),
(0, 133, '2019-11-29 13:49:13', 1, 0),
(0, 134, '2019-11-29 13:49:14', 1, 0),
(0, 135, '2019-11-29 13:49:14', 1, 0),
(0, 136, '2019-11-29 13:49:15', 1, 0),
(0, 137, '2019-11-29 13:49:16', 2, 0),
(0, 138, '2019-11-29 13:49:16', 4, 2),
(0, 139, '2019-11-29 13:49:17', 0, 5),
(0, 140, '2019-11-29 13:49:17', 2, 3),
(0, 141, '2019-11-29 13:50:18', 2, 0),
(0, 142, '2019-11-29 13:50:20', 1, 0),
(0, 143, '2019-11-29 13:50:22', 4, 0),
(0, 144, '2019-11-29 13:50:25', 18, 0),
(0, 145, '2019-11-29 13:50:27', 27, 1),
(0, 146, '2019-11-29 13:50:29', 24, 0),
(0, 147, '2019-11-29 13:50:32', 27, 0),
(0, 148, '2019-11-29 13:50:34', 25, 1),
(0, 149, '2019-11-29 13:50:36', 39, 1),
(0, 150, '2019-11-29 13:50:39', 80, 1),
(0, 151, '2019-11-29 13:50:43', 1, 0),
(0, 152, '2019-11-29 13:50:45', 1, 0),
(0, 153, '2019-11-29 13:50:47', 1, 0),
(0, 154, '2019-11-29 13:50:50', 3, 0),
(0, 155, '2019-11-29 13:50:52', 1, 3),
(0, 156, '2019-11-29 13:50:55', 1, 0),
(0, 157, '2019-11-29 13:50:57', 3, 2),
(0, 158, '2019-11-29 13:50:59', 1, 2),
(0, 159, '2019-11-29 13:51:02', 1, 0),
(0, 160, '2019-11-29 13:51:04', 1, 2),
(0, 161, '2019-11-29 13:51:37', 2, 0),
(0, 162, '2019-11-29 13:51:39', 2, 0),
(0, 163, '2019-11-29 13:51:41', 10, 1),
(0, 164, '2019-11-29 13:51:44', 7, 1),
(0, 165, '2019-11-29 13:51:46', 5, 0),
(0, 166, '2019-11-29 13:51:48', 20, 0),
(0, 167, '2019-11-29 13:51:50', 33, 1),
(0, 168, '2019-11-29 13:51:53', 26, 0),
(0, 169, '2019-11-29 13:51:55', 29, 0),
(0, 170, '2019-11-29 13:51:57', 25, 1),
(0, 171, '2019-11-29 13:52:00', 1, 1),
(0, 172, '2019-11-29 13:52:03', 2, 0),
(0, 173, '2019-11-29 13:52:05', 0, 1),
(0, 174, '2019-11-29 13:52:07', 1, 4),
(0, 175, '2019-11-29 13:52:09', 1, 0),
(0, 176, '2019-11-29 13:52:11', 4, 0),
(0, 177, '2019-11-29 13:52:14', 1, 5),
(0, 178, '2019-11-29 13:52:16', 1, 0),
(0, 179, '2019-11-29 13:52:18', 3, 3),
(0, 180, '2019-11-29 13:52:20', 1, 2),
(0, 181, '2019-11-29 13:52:53', 4, 0),
(0, 182, '2019-11-29 13:52:55', 5, 0),
(0, 183, '2019-11-29 13:52:57', 18, 2),
(0, 184, '2019-11-29 13:52:59', 11, 1),
(0, 185, '2019-11-29 13:53:01', 8, 0),
(0, 186, '2019-11-29 13:53:03', 20, 1),
(0, 187, '2019-11-29 13:53:05', 39, 1),
(0, 188, '2019-11-29 13:53:08', 28, 1),
(0, 189, '2019-11-29 13:53:10', 30, 0),
(0, 190, '2019-11-29 13:53:12', 27, 1),
(0, 191, '2019-11-29 13:53:15', 1, 0),
(0, 192, '2019-11-29 13:53:17', 1, 0),
(0, 193, '2019-11-29 13:53:19', 1, 1),
(0, 194, '2019-11-29 13:53:21', 2, 0),
(0, 195, '2019-11-29 13:53:23', 1, 0),
(0, 196, '2019-11-29 13:53:25', 1, 1),
(0, 197, '2019-11-29 13:53:27', 2, 1),
(0, 198, '2019-11-29 13:53:29', 1, 1),
(0, 199, '2019-11-29 13:53:32', 1, 7),
(0, 200, '2019-11-29 13:53:34', 3, 1),
(0, 201, '2019-11-29 14:15:10', 4, 0),
(0, 202, '2019-11-29 14:15:12', 2, 0),
(0, 203, '2019-11-29 14:19:08', 5, 1),
(0, 204, '2019-11-29 14:19:08', 14, 0),
(0, 205, '2019-11-29 14:19:09', 5, 0),
(0, 206, '2019-11-29 14:19:09', 11, 1),
(0, 207, '2019-11-29 14:19:10', 10, 0),
(0, 208, '2019-11-29 14:19:11', 27, 1),
(0, 209, '2019-11-29 14:19:11', 24, 3),
(0, 210, '2019-11-29 14:19:12', 25, 0),
(0, 211, '2019-11-29 14:19:12', 29, 3),
(0, 212, '2019-11-29 14:19:13', 23, 1),
(0, 213, '2019-11-29 14:19:14', 1, 1),
(0, 214, '2019-11-29 14:19:15', 1, 0),
(0, 215, '2019-11-29 14:19:15', 1, 0),
(0, 216, '2019-11-29 14:19:16', 2, 2),
(0, 217, '2019-11-29 14:19:16', 1, 1),
(0, 218, '2019-11-29 14:19:17', 2, 0),
(0, 219, '2019-11-29 14:19:17', 1, 0),
(0, 220, '2019-11-29 14:19:18', 1, 1),
(0, 221, '2019-11-29 14:19:19', 1, 0),
(0, 222, '2019-11-29 14:19:19', 2, 1),
(0, 223, '2019-11-29 14:24:13', 3, 0);

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `subreddit`
--

CREATE TABLE `subreddit` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `subreddit`
--

INSERT INTO `subreddit` (`id`, `name`) VALUES
(1, 'dankmemes'),
(2, 'askreddit');

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `posthistoryelement`
--
ALTER TABLE `posthistoryelement`
  ADD PRIMARY KEY (`id`);

--
-- Indizes für die Tabelle `subreddit`
--
ALTER TABLE `subreddit`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `post`
--
ALTER TABLE `post`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;

--
-- AUTO_INCREMENT für Tabelle `posthistoryelement`
--
ALTER TABLE `posthistoryelement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=224;

--
-- AUTO_INCREMENT für Tabelle `subreddit`
--
ALTER TABLE `subreddit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
