"""
Generic methods which are used in several Inputs.
"""


from __future__ import annotations

import asyncpraw  # type: ignore


class GenericRedditTools:
    """
    Tools for reddit mixin.
    """

    @staticmethod
    def render_submission(
        reddit_submission: asyncpraw.reddit.Submission, prefix: str = "subreddit"
    ) -> str:
        """
        Produce a human-readable version of a reddit submission.

        :param reddit_submission:
        :param prefix: To prepend to all the printed lines
        :return:
        """
        submission_contents = [
            f"{prefix}_submission.id: {reddit_submission.id}",
            f"{prefix}_submission.subreddit: {reddit_submission.subreddit}",
            f"{prefix}_submission.name: {reddit_submission.name}",
            f"{prefix}_submission.title: {reddit_submission.title}",
            f"{prefix}_submission.author: {reddit_submission.author}",
            f"{prefix}_submission.stickied: {reddit_submission.stickied}",
            f"{prefix}_submission.selftext: {reddit_submission.selftext}",
            f"{prefix}_submission.url: {reddit_submission.url}",
        ]
        return "\n".join(submission_contents)

    @staticmethod
    def render_comment(
        reddit_comment: asyncpraw.reddit.Comment, prefix: str = "subreddit"
    ) -> str:
        """
        Produce a human-readable version of a reddit comment.

        :param reddit_comment:
        :param prefix: The prefix for all the printed info lines
        :return:
        """
        comment_contents = [
            f"{prefix}_comment.id: {reddit_comment.id}",
            f"{prefix}_comment.author: {reddit_comment.author}",
            f"{prefix}_comment.body: {reddit_comment.body}",
            f"{prefix}_comment.created_utc: {reddit_comment.created_utc}",
            f"{prefix}_comment.distinguished: {reddit_comment.distinguished}",
            f"{prefix}_comment.edited: {reddit_comment.edited}",
            f"{prefix}_comment.is_submitter: {reddit_comment.is_submitter}",
            f"{prefix}_comment.subreddit_id: {reddit_comment.subreddit_id}",
        ]
        return "\n".join(comment_contents)

    @staticmethod
    def hash_comment(reddit_comment: asyncpraw.reddit.Comment) -> str:
        """
        Take a comment and return a hash for it.

        This is pretty simple - just a str of a tuple of the comment_id and contents
        :param reddit_comment:
        :return:
        """
        return str((reddit_comment.id, reddit_comment.body))

    @staticmethod
    def hash_submission(submission_comment: asyncpraw.reddit.Submission) -> str:
        """
        Take a comment and return a hash for it.

        This is pretty simple - just a str of a tuple of the comment_id and contents
        :param submission_comment:
        :return:
        """
        return str(
            (submission_comment.id, submission_comment.selftext, submission_comment.author)
        )
