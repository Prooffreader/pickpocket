# pickpocket [in development, pre-alpha]
Python app to pick an item from your Pocket account and e-mail it to you to force you to read it

<img src="https://www.dtdata.io/shared/pocket.svg" alt="Pocket logo" width="75">

Pocket (formerly Read It Later) and similar bookmarking apps are great, but in my and many users' experience they tend to become a dumping ground for stuff that you rarely if ever return to, maybe sometimes taking a few hours to curate the backlog in a herculean effort.

So I came up with this Python app that will, e.g. on a cron job, grab a bookmark at random and e-mail it to you (at present, the only outgoing e-mail provider supported is gmail. You could create an account just for this). It also **erases the bookmark from Pocket**, so you've got no choice but to read it!

Future todos:
* accommodate more general smtp than/as well as gmail
* allow option of ~/.yagmail config instead of .env
* assuming you have a custom e-mail, have a config option that lets you reply to the email to put the link back *as a favorite.*. At least that way *some* triage will happen
* make a webhook to trigger it (although that's really outside scope, a separate implementation concern)
