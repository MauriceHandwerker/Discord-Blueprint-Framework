# Discord-Blueprint-Framework
Plan you Discord server with your friends and team members and create a Blueprint that everybody understands.

### Why DBF ?
DBF aka. Discord Blueprint Framework is a simple way to discribe a Discord server in a txt file. 
Its really easy to read and understand so that you can easily plan and build a Discord server with your friends, colligues or clup members.
It works in every language and every Discord Bot available.


### Content
[1. Why DBF ?](#why-dbf)\
[2. Content](#content)\
[3. Demo](#demo)\
[4. Structure](STRUCTURE.md)\
[5. Categories](CATEGORIES.md)\
[6. Chanals](CHANALS.md)\
[7. Roles](ROLES.md)\
[8. Permissions](PERMISSIONS.md)\
[9. Bots](BOTS.md)

### Demo
```
$$ project demo

ROLES = {
	/ Owner	[ All; light red ]
	/ Co.Owner [ All; red ]
	/ Bot [ All; cyan ]
	/ Marketing Manager [ ; yellow ]
	/ Team Manager [ ; yellow ]
	/ Team 1 Leader [ ; dark blue ]
	/ Team 1 Member [ ; light blue ]
	/ Supporter [ ; green ]
}

SERVER = [ Support System, ProBot ]{

	# Tickets [ Support, Team 1 Leader, Team 1 Manager, Marketing Manager, Bot, Co.Owner, Owner, @user ]
	
	# Global [ All ]
		- welcome [ Co.Owner, Owner, Bot ]
		- news [ Co.Owner, Owner, Bot ]
		- global chat [ All ]
		+ voice 1 [ All ]
		+ voice 2 [ All ]
		+ voice 3
	
	# Team 1 [ Team Manager, Team 1 Leader, Team 1 Member, Co.Owner, Owner, Bot ]
		- team news [ Team Manager, Team 1 Leader, Co.Owner, Owner, Bot ]
		- team chat [ All ]
		- team notes [ All ]
		+ voice [ All ]
		+ meeting [ All ]
		+ tournament [ All ]
	
	# High Team [ Marketing Manager, Team Manager, Co.Owner, Owner, Bot ]
		- high team news [ Co.Owner, Owner, Bot ]
		- high team notes [ All ]
		- high team chat [ All ]
		+ high team voice [ All ]
		+ high team meeting	[ All ]
	
	# Team [ Supporter, Team Manager, Marketing Manager, Co.Owner, Owner, Bot ]
		- team news [ Co.Owner, Owner, Bot ]
		- team ideas [ All ]
		- team chat [ All ]
		+ voice [ All ]
		+ meeting [ All ]
	
	# Support [ All ]
		- tickets [ All, BOT: "Support System", =; ]
			= Join Team
			= Join Team 1
			= Questions
			= Report
	
}
```
