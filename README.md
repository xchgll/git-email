# Git-Email

![Snippet](/snippet.png)

- **`Git-Email` is a tool to extract emails and other info from repositry commits**
- **you can search in all repos or specific repo**

## Search in specific repostiry

```
> python git-email.py -u torvalds -r linux -v 1

  ________.__  __            ___________              .__.__   
 /  _____/|__|/  |_          \_   _____/ _____ _____  |__|  |  
/   \  ___|  \   __\  ______  |    __)_ /     \\__  \ |  |  |  
\    \_\  \  ||  |   /_____/  |        \  Y Y  \/ __ \|  |  |__
 \______  /__||__|           /_______  /__|_|  (____  /__|____/
        \/                           \/      \/     \/         

Author: @xchgll

[~] Target: torvalds
[+] Found 1 repositories


____REPO____
Name:    linux
URL:     https://github.com/torvalds/linux
Stars:   237556
Private: False
Created: 2011-09-04T22:48:12Z
Updated: 2026-06-25T22:09:16Z

========== Unique Emails Found ==========
  [>] torvalds  torvalds@linux-foundation.org
  [>] kuba-moo  kuba@kernel.org
[+] Total: 2 unique email(s)

```

## Increasing Verbosity (More Detailed)

```
> python git-email.py -u torvalds -r linux -v 2

  ________.__  __            ___________              .__.__   
 /  _____/|__|/  |_          \_   _____/ _____ _____  |__|  |  
/   \  ___|  \   __\  ______  |    __)_ /     \\__  \ |  |  |  
\    \_\  \  ||  |   /_____/  |        \  Y Y  \/ __ \|  |  |__
 \______  /__||__|           /_______  /__|_|  (____  /__|____/
        \/                           \/      \/     \/         

Author: @xchgll

[~] Target: torvalds
[+] Found 1 repositories


____REPO____
Name:    linux
URL:     https://github.com/torvalds/linux
Stars:   237555
Private: False
Created: 2011-09-04T22:48:12Z
Updated: 2026-06-25T21:53:06Z
[*] Fetching commits from: https://api.github.com/repos/torvalds/linux/commits
Hash:      4edcdefd4083ae04b1a5656f4be6cd83ae919ef4
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/4edcdefd4083ae04b1a5656f4be6cd83ae919ef4


Hash:      8c04c1292dca29a57ea82c6a44348be49749fc22
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/8c04c1292dca29a57ea82c6a44348be49749fc22


Hash:      ca3e303061a4abbb92cf306aea2057c59a734757
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/ca3e303061a4abbb92cf306aea2057c59a734757


Hash:      75218b7acec35b0306572bf5fdf179486d463c9e
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/75218b7acec35b0306572bf5fdf179486d463c9e


Hash:      805185b7c7a1069e407b6f7b3bc98e44d415f484
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/805185b7c7a1069e407b6f7b3bc98e44d415f484


Hash:      c75597caada080effbfbc0a7fb10dc2a3bb543ad
Author:    torvalds
Committer: torvalds
Email:     torvalds@linux-foundation.org
URL:       https://github.com/torvalds/linux/commit/c75597caada080effbfbc0a7fb10dc2a3bb543ad


Hash:      fe9f4ee6c61a1410afd73bf011de5ae618004796
Author:    kuba-moo
Committer: kuba-moo
Email:     kuba@kernel.org
URL:       https://github.com/torvalds/linux/commit/fe9f4ee6c61a1410afd73bf011de5ae618004796
...........
```

## Search in all repositries

```
> python git-email.py -u torvalds              

  ________.__  __            ___________              .__.__   
 /  _____/|__|/  |_          \_   _____/ _____ _____  |__|  |  
/   \  ___|  \   __\  ______  |    __)_ /     \\__  \ |  |  |  
\    \_\  \  ||  |   /_____/  |        \  Y Y  \/ __ \|  |  |__
 \______  /__||__|           /_______  /__|_|  (____  /__|____/
        \/                           \/      \/     \/         

Author: @xchgll

[~] Target: torvalds
[+] Found 12 repositories


____REPO____
Name:    1590A
URL:     https://github.com/torvalds/1590A
Stars:   568
Private: False
Created: 2025-03-01T04:36:29Z
Updated: 2026-06-25T00:42:31Z

____REPO____
Name:    AudioNoise
URL:     https://github.com/torvalds/AudioNoise
Stars:   4388
Private: False
Created: 2026-01-09T02:33:29Z
Updated: 2026-06-25T01:25:27Z

____REPO____
Name:    GuitarPedal
URL:     https://github.com/torvalds/GuitarPedal
Stars:   2036
Private: False
Created: 2025-09-17T01:01:29Z
Updated: 2026-06-25T21:07:31Z

____REPO____
Name:    HunspellColorize
URL:     https://github.com/torvalds/HunspellColorize
Stars:   348
Private: False
Created: 2026-01-18T19:57:03Z
Updated: 2026-06-23T15:38:58Z

____REPO____
Name:    libdc-for-dirk
URL:     https://github.com/torvalds/libdc-for-dirk
Stars:   393
Private: False
Created: 2017-01-17T00:25:49Z
Updated: 2026-06-23T18:32:22Z

____REPO____
Name:    libgit2
URL:     https://github.com/torvalds/libgit2
Stars:   366
Private: False
Created: 2022-07-30T03:30:56Z
Updated: 2026-06-25T00:42:30Z

____REPO____
Name:    linux
URL:     https://github.com/torvalds/linux
Stars:   237557
Private: False
Created: 2011-09-04T22:48:12Z
Updated: 2026-06-25T22:20:17Z

____REPO____
Name:    pesconvert
URL:     https://github.com/torvalds/pesconvert
Stars:   565
Private: False
Created: 2017-12-04T21:58:56Z
Updated: 2026-06-23T18:32:25Z

____REPO____
Name:    ScrollWheel
URL:     https://github.com/torvalds/ScrollWheel
Stars:   335
Private: False
Created: 2026-06-02T15:48:56Z
Updated: 2026-06-25T21:35:27Z

____REPO____
Name:    subsurface-for-dirk
URL:     https://github.com/torvalds/subsurface-for-dirk
Stars:   463
Private: False
Created: 2017-01-11T18:03:01Z
Updated: 2026-06-23T18:32:24Z

____REPO____
Name:    test-tlb
URL:     https://github.com/torvalds/test-tlb
Stars:   1019
Private: False
Created: 2017-03-24T20:06:37Z
Updated: 2026-06-25T21:51:43Z

____REPO____
Name:    uemacs
URL:     https://github.com/torvalds/uemacs
Stars:   2059
Private: False
Created: 2018-01-17T22:32:21Z
Updated: 2026-06-24T21:27:25Z

========== Unique Emails Found ==========
  [>] torvalds  torvalds@linux-foundation.org
  [>] web-flow  noreply@github.com
  [>] dirkhh  dirk@hohndel.org
  [>] jefdriesen  jefdriesen@users.sourceforge.net
  [>] ethomson  ethomson@edwardthomson.com
  [>] boretrk  boretrk@hotmail.com
  [>] kuba-moo  kuba@kernel.org
  [>] MaxKellermann  max.kellermann@gmail.com
  [>] atdotde  helling@atdotde.de
[+] Total: 9 unique email(s)
```


## Download

```
wget https://github.com/xchgll/git-email/raw/refs/heads/master/git-email.py
python git-emai.py -h
```