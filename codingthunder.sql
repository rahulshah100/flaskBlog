-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 31, 2020 at 09:28 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingthunder`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `sno` int(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone_num` int(50) NOT NULL,
  `date` datetime(6) DEFAULT current_timestamp(6),
  `msg` text NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`sno`, `name`, `phone_num`, `date`, `msg`, `email`) VALUES
(1, 'my name', 2147483647, '2020-05-30 13:20:50.432108', 'this is mssg', 'ssender_email'),
(2, '21w', 2147483647, '2020-05-30 13:46:12.662028', 'yes my message\r\n', 'ds@sd');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(50) NOT NULL,
  `title` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `date` datetime DEFAULT current_timestamp(),
  `slug` varchar(50) NOT NULL,
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `content`, `date`, `slug`, `img_file`) VALUES
(1, 'This is my Title 1', 'here i was mentioning a date column & then didnt passed it back class\'s object,but just not mentioning a date column in class		also does the trick & we dont need to pass anythinh in object but Current_TimeStamp will do the thing  -> created table contacts with sno(a.i. & primary key),name,phone_nu,.msg,date(default:current timeStamp	 & null),email & each of these columns are allocated appropriate lengths & type   -> Also note ive allocated types as text for few columns ,text is just similar to varchar but ', '2020-05-31 23:23:26', 'slug1', 'img/about-bg.jpg'),
(2, 's & type    -> Also note ive allocated types as te', 'ut here null is received & is considered \r\n		for which i imported datetime module in python and sent date=datetime.now() from flask to db.\r\n		Tho still here i was mentioning a date column & then didnt passed it back class\'s object,but just not mentioning a date column in class\r\n		also does the trick & we dont need to pass anythinh in object but Current_TimeStamp will do the thing\r\n  -> created table contacts with sno(a.i. & primary key),name,phone_nu,.msg,date(default:current timeStam', '2020-05-30 12:56:39', 'slug2', 'img/home-bg.jpg'),
(3, 'As i wanted to make posts on my home page configur', ' consistent structure is formed where a for loop with jinja templating can be used\r\n	   and placed this passed variable\'s different parts at diff. places\r\n	-> Added 5 more posts in posts table so then i can check if i can control no. of posts to be displayed \r\n	-> in app.route(\"/\") limite', '2020-05-30 13:16:43', 'slug3', 'img/home-bg.jpg'),
(4, 'Title4 : Also note ive allocated types as te', '->Examples->sigin template->copy pasted it\'s source code to login.html(a new file)in templates folder\r\n		also for some link which were not https://...(i.e one\'s which werenot fetched from net but from local machines\'folder) clicked on them\r\n		& copy pasted/save as them in static/css as bootstrap.min.css & floating-label.css.Then removed some more dead links which console of browser\r\n		showed werent able to be loaded from link as those links also referred to local machine\'s folder.\r\n		Edited some html text & added a lil css to padding left & right the 2 i/p boxes visible on this page\r\n	-> Made an endpoint in .py file called dashboard tht\'ll ret', '2020-05-30 13:16:43', 'slug4', 'img/about-bg.jpg'),
(5, 'Title5 ing a parameter of date send null from flas', ' Added new parameter in config.json for no_of_posts\r\n	-> As i wanted to make posts on my home page configurable & fetchable from db so,in app.route(\'/\') i made a variable which fetched entire posts table\r\n	-> passing this variable to index.html i recreated it\'s Main Content part in a way tht a consistent structure is formed where a for loop with jinja templating can be used\r\n	   and placed this passed variable\'s different parts at diff. places\r\n	-> Added 5 more posts in posts table so then i can check if i can control no. of posts to be displayed \r\n	-> in app.route(\"/\") limited no. of posts by taking configurable parameter no_of_post from config.json\r\n	\r\n	Part 9\r\n	-> Went to get bootstrap->Examples->sigin template->copy pasted it\'s source code to login.html(a new file)in templates folder\r\n		also for some link which were not https://...(i.e one\'s which werenot fetched from net but from local machines\'folder) clicked on them', '2020-05-30 13:18:09', 'slulg5', 'img/home-bg.jpg'),
(6, 'Title6 copy pasted/save as them in static/css as b', 'showed werent able to be loaded from link as those links also referred to local machine\'s folder.\r\n		Edited some html text & added a lil css to padding left & right the 2 i/p boxes visible on this page\r\n	-> Made an endpoint in .py file called dashboard tht\'ll return this page login.html', '2020-05-30 13:18:09', 'slug6', 'img/about-bg.jpg'),
(7, ',in app.route(\'/\') i made a variable which fetched', 'so what we need to do to use Get method in flask \r\n		provide method=\'get\' or not writing anything in form & methods=\"GET\" or not writing anything in app.route\r\n		thn fetching inputted element by var = request.args.get(name_of_input_text_in_form).\r\n		Also it would be seen how name & va;ue travels in link using get method', '2020-05-30 13:19:02', 'slug7', 'img/about-bg.jpg'),
(8, 'Outside Title', 'outside Contenttt', '2020-05-30 14:40:56', 'outsideslug', 'oioi.jpg'),
(10, 'Ninth Post\'s Title ,this is', 'svbupwueqfwe njvnwe[v jw vjwvw\r\nrgwfwegwrb46tn\r\nwtnwrbhrwywnnjmtenwrym\r\nwy rwt trtneynwtnhw4errwybmnwrbtebbet\r\nhwtnqtnwt', '2020-05-31 16:00:00', 'sulg9', 'img/about-bg.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
