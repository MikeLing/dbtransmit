DROP DATABASE IF EXISTS sbtest1;
CREATE DATABASE sbtest1;
USE  sbtest1;
DROP TABLE IF EXISTS t1;
CREATE TABLE t1
(
  place_id int (10) unsigned NOT NULL,
  shows int(10) unsigned DEFAULT '0' NOT NULL,
  ishows int(10) unsigned DEFAULT '0' NOT NULL,
  ushows int(10) unsigned DEFAULT '0' NOT NULL,
  clicks int(10) unsigned DEFAULT '0' NOT NULL,
  iclicks int(10) unsigned DEFAULT '0' NOT NULL,
  uclicks int(10) unsigned DEFAULT '0' NOT NULL,
  ts timestamp,
  PRIMARY KEY (place_id,ts)
);

INSERT INTO t1 (place_id,shows,ishows,ushows,clicks,iclicks,uclicks,ts) VALUES (1,0,0,0,0,0,0,20000928174434);
