CREATE DATABASE ikea_analytics;

\c ikea_analytics;

CREATE TABLE tweets(
   id bigint,
   text text,
   created_at timestamp,
   retweet_count smallint,
   reply_count smallint,
   like_count smallint,
   quote_count smallint
);