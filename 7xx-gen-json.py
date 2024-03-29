#!/usr/bin/env python3

s = """
## Inexcusable

  - 701 - Meh
  - 702 - Emacs
  - 703 - Explosion
  - 704 - Goto Fail
  - 705 - I wrote the code and missed the necessary validation by an oversight (see 795)
  - 706 - Delete Your Account
  - 707 - Can't quit vi

## Novelty Implementations

  - 710 - PHP
  - 711 - Convenience Store
  - 712 - NoSQL
  - 718 - I am not a teapot
  - 719 - Haskell

## Edge Cases

  - 720 - Unpossible
  - 721 - Known Unknowns
  - 722 - Unknown Unknowns
  - 723 - Tricky
  - 724 - This line should be unreachable
  - 725 - It works on my machine
  - 726 - It's a feature, not a bug
  - 727 - 32 bits is plenty
  - 728 - It works in my timezone

## Fucking

  - 730 - Fucking npm
  - 731 - Fucking Rubygems
  - 732 - Fucking Unic💩de
  - 733 - Fucking Deadlocks
  - 734 - Fucking Deferreds
  - 736 - Fucking Race Conditions
  - 735 - Fucking IE
  - 737 - FuckThreadsing
  - 738 - Fucking Exactly-once Delivery
  - 739 - Fucking Windows
  - 738 - Fucking Exactly-once Delivery
  - 739 - Fucking McAfee

## Reserved for meritocracy related bullshit

  74x TBD. Got the brains trust on the case.

## Syntax Errors

  - 750 - Didn't bother to compile it
  - 753 - Syntax Error
  - 754 - Too many semi-colons
  - 755 - Not enough semi-colons
  - 756 - Insufficiently polite
  - 757 - Excessively polite
  - 759 - Unexpected `T_PAAMAYIM_NEKUDOTAYIM`

## Substance-Affected Developer

  - 761 - Hungover
  - 762 - Stoned
  - 763 - Under-Caffeinated
  - 764 - Over-Caffeinated
  - 765 - Railscamp
  - 766 - Sober
  - 767 - Drunk
  - 768 - Accidentally Took Sleeping Pills Instead Of Migraine Pills During Crunch Week

## Predictable Problems

  - 771 - Cached for too long
  - 772 - Not cached long enough
  - 773 - Not cached at all
  - 774 - Why was this cached?
  - 775 - Out of cash
  - 776 - Error on the Exception
  - 777 - Coincidence
  - 778 - Off By One Error
  - 779 - Off By Too Many To Count Error

## Somebody Else's Problem

  - 780 - Project owner not responding
  - 781 - Operations
  - 782 - QA
  - 783 - It was a customer request, honestly
  - 784 - Management, obviously
  - 785 - TPS Cover Sheet not attached
  - 786 - Try it now
  - 787 - Further Funding Required
  - 788 - Designer's final designs weren't
  - 789 - Not my department

## Internet crashed

  - 791 - The Internet shut down due to copyright restrictions
  - 792 - Climate change driven catastrophic weather event
  - 793 - Zombie Apocalypse
  - 794 - Someone let PG near a REPL
  - 795 - #heartbleed (see 705)
  - 796 - Some DNS fuckery idno
  - 797 - This is the last page of the Internet. Go back
  - 798 - I checked the db backups cupboard and the cupboard was bare
  - 799 - End of the world
"""
s = s.split("\n")
s = [l.strip()[2:].split("-") for l in s if l.strip().startswith("-")]
n = []
for a in s:
    n.append([a[0], "-".join(a[1:])])
s = [[i.strip() for i in a] for a in n]
    
import json
with open("7xx-errors.json", "wb") as f:
    f.write(json.dumps(s, sort_keys=True, indent=4).encode())

