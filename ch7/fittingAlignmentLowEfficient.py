


<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# githubog: http://ogp.me/ns/fb/githubog#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>bioinformatics_algorithms1_coursera_2013_ucsd/ch7/fittingAlignment.py at master · biomystery/bioinformatics_algorithms1_coursera_2013_ucsd</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub" />
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub" />
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png" />
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png" />
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png" />
    <link rel="logo" type="image/svg" href="https://github-media-downloads.s3.amazonaws.com/github-logo.svg" />
    <meta property="og:image" content="https://github.global.ssl.fastly.net/images/modules/logos_page/Octocat.png">
    <meta name="hostname" content="github-fe117-cp1-prd.iad.github.net">
    <meta name="ruby" content="ruby 1.9.3p194-tcs-github-tcmalloc (a846054d10) [x86_64-linux]">
    <link rel="assets" href="https://github.global.ssl.fastly.net/">
    <link rel="conduit-xhr" href="https://ghconduit.com:25035/">
    <link rel="xhr-socket" href="/_sockets" />
    


    <meta name="msapplication-TileImage" content="/windows-tile.png" />
    <meta name="msapplication-TileColor" content="#ffffff" />
    <meta name="selected-link" value="repo_source" data-pjax-transient />
    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="84EF4779:06F2:7BC6441:52CD9E88" name="octolytics-dimension-request_id" /><meta content="1592000" name="octolytics-actor-id" /><meta content="biomystery" name="octolytics-actor-login" /><meta content="be81fbaf9dd8190aa6b59ef35fc3409cb509c4a66edb3c46175a10062c47f030" name="octolytics-actor-hash" />
    

    
    
    <link rel="icon" type="image/x-icon" href="/favicon.ico" />

    <meta content="authenticity_token" name="csrf-param" />
<meta content="7e4A2FbZl3W7x6MA2Xa5oAF37zPn0I6Wv2dzeJmilK4=" name="csrf-token" />

    <link href="https://github.global.ssl.fastly.net/assets/github-97a08d0c62ded290cae46fd72fc0a38c835777a6.css" media="all" rel="stylesheet" type="text/css" />
    <link href="https://github.global.ssl.fastly.net/assets/github2-e9fa70a28908749635706b3edcc1dad6bfaa378c.css" media="all" rel="stylesheet" type="text/css" />
    

    

      <script src="https://github.global.ssl.fastly.net/assets/frameworks-7d67be4fc516c4502a4685bd4c55f014cca4eb36.js" type="text/javascript"></script>
      <script src="https://github.global.ssl.fastly.net/assets/github-a31c5b367955deef4f0ee1d5b5e90e9edfc7fba5.js" type="text/javascript"></script>
      
      <meta http-equiv="x-pjax-version" content="874518d40f47c7b1792d9c24a93a503b">

        <link data-pjax-transient rel='permalink' href='/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/blob/803cf0f27815bc6cad664d1ce62662c2c802fb91/ch7/fittingAlignment.py'>
  <meta property="og:title" content="bioinformatics_algorithms1_coursera_2013_ucsd"/>
  <meta property="og:type" content="githubog:gitrepository"/>
  <meta property="og:url" content="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd"/>
  <meta property="og:image" content="https://github.global.ssl.fastly.net/images/gravatars/gravatar-user-420.png"/>
  <meta property="og:site_name" content="GitHub"/>
  <meta property="og:description" content="Contribute to bioinformatics_algorithms1_coursera_2013_ucsd development by creating an account on GitHub."/>

  <meta name="description" content="Contribute to bioinformatics_algorithms1_coursera_2013_ucsd development by creating an account on GitHub." />

  <meta content="1592000" name="octolytics-dimension-user_id" /><meta content="biomystery" name="octolytics-dimension-user_login" /><meta content="14565197" name="octolytics-dimension-repository_id" /><meta content="biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="14565197" name="octolytics-dimension-repository_network_root_id" /><meta content="biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/commits/master.atom" rel="alternate" title="Recent Commits to bioinformatics_algorithms1_coursera_2013_ucsd:master" type="application/atom+xml" />

  </head>


  <body class="logged_in  env-production macintosh vis-public page-blob">
    <div class="wrapper">
      
      
      
      


      <div class="header header-logged-in true">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/">
  <span class="mega-octicon octicon-mark-github"></span>
</a>

    
    <a href="/notifications" class="notification-indicator tooltipped downwards" data-gotokey="n" title="You have unread notifications">
        <span class="mail-status unread"></span>
</a>

      <div class="command-bar js-command-bar  in-repository">
          <form accept-charset="UTF-8" action="/search" class="command-bar-form" id="top_search_form" method="get">

<input type="text" data-hotkey="/ s" name="q" id="js-command-bar-field" placeholder="Search or type a command" tabindex="1" autocapitalize="off"
    
    data-username="biomystery"
      data-repo="biomystery/bioinformatics_algorithms1_coursera_2013_ucsd"
      data-branch="master"
      data-sha="ddb8af898f6e8fc4af27bd7d694f5e97089d11c3"
  >

    <input type="hidden" name="nwo" value="biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" />

    <div class="select-menu js-menu-container js-select-menu search-context-select-menu">
      <span class="minibutton select-menu-button js-menu-target">
        <span class="js-select-button">This repository</span>
      </span>

      <div class="select-menu-modal-holder js-menu-content js-navigation-container">
        <div class="select-menu-modal">

          <div class="select-menu-item js-navigation-item js-this-repository-navigation-item selected">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" class="js-search-this-repository" name="search_target" value="repository" checked="checked" />
            <div class="select-menu-item-text js-select-button-text">This repository</div>
          </div> <!-- /.select-menu-item -->

          <div class="select-menu-item js-navigation-item js-all-repositories-navigation-item">
            <span class="select-menu-item-icon octicon octicon-check"></span>
            <input type="radio" name="search_target" value="global" />
            <div class="select-menu-item-text js-select-button-text">All repositories</div>
          </div> <!-- /.select-menu-item -->

        </div>
      </div>
    </div>

  <span class="octicon help tooltipped downwards" title="Show command bar help">
    <span class="octicon octicon-question"></span>
  </span>


  <input type="hidden" name="ref" value="cmdform">

</form>
        <ul class="top-nav">
          <li class="explore"><a href="/explore">Explore</a></li>
            <li><a href="https://gist.github.com">Gist</a></li>
            <li><a href="/blog">Blog</a></li>
          <li><a href="https://help.github.com">Help</a></li>
        </ul>
      </div>

    


  <ul id="user-links">
    <li>
      <a href="/biomystery" class="name">
        <img height="20" src="https://0.gravatar.com/avatar/a1574873074d962564e1436d308d0243?d=https%3A%2F%2Fidenticons.github.com%2F270a598bc10d96e5224988fd04ce3c14.png&amp;r=x&amp;s=140" width="20" /> biomystery
      </a>
    </li>

      <li class="new-menu dropdown-toggle js-menu-container">
        <a href="#" class="js-menu-target" class="tooltipped downwards" title="New repo, org, etc">
          <span class="octicon octicon-plus"></span>
          <span class="dropdown-arrow"></span>
        </a>

        <div class="js-menu-content">
        </div>
      </li>

      <li>
        <a href="/settings/profile" id="account_settings"
          class="tooltipped downwards"
          aria-label="Account settings "
          title="Account settings ">
          <span class="octicon octicon-tools"></span>
        </a>
      </li>
      <li>
        <a class="tooltipped downwards" href="/logout" data-method="post" id="logout" title="Sign out" aria-label="Sign out">
          <span class="octicon octicon-log-out"></span>
        </a>
      </li>

  </ul>

<div class="js-new-dropdown-contents hidden">
  

<ul class="dropdown-menu">
  <li>
    <a href="/new"><span class="octicon octicon-repo-create"></span> New repository</a>
  </li>
  <li>
    <a href="/organizations/new"><span class="octicon octicon-organization"></span> New organization</a>
  </li>



    <li class="section-title">
      <span title="biomystery/bioinformatics_algorithms1_coursera_2013_ucsd">This repository</span>
    </li>
      <li>
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/issues/new"><span class="octicon octicon-issue-opened"></span> New issue</a>
      </li>
      <li>
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/settings/collaboration"><span class="octicon octicon-person-add"></span> New collaborator</a>
      </li>
</ul>

</div>


    
  </div>
</div>

      

      




          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    
    <div class="pagehead repohead instapaper_ignore readability-menu">
      <div class="container">
        

<ul class="pagehead-actions">

    <li class="subscription">
      <form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="7e4A2FbZl3W7x6MA2Xa5oAF37zPn0I6Wv2dzeJmilK4=" /></div>  <input id="repository_id" name="repository_id" type="hidden" value="14565197" />

    <div class="select-menu js-menu-container js-select-menu">
      <a class="social-count js-social-count" href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/watchers">
        1
      </a>
      <span class="minibutton select-menu-button with-count js-menu-target" role="button" tabindex="0">
        <span class="js-select-button">
          <span class="octicon octicon-eye-unwatch"></span>
          Unwatch
        </span>
      </span>

      <div class="select-menu-modal-holder">
        <div class="select-menu-modal subscription-menu-modal js-menu-content">
          <div class="select-menu-header">
            <span class="select-menu-title">Notification status</span>
            <span class="octicon octicon-remove-close js-menu-close"></span>
          </div> <!-- /.select-menu-header -->

          <div class="select-menu-list js-navigation-container" role="menu">

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_included" name="do" type="radio" value="included" />
                <h4>Not watching</h4>
                <span class="description">You only receive notifications for conversations in which you participate or are @mentioned.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-watch"></span>
                  Watch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input checked="checked" id="do_subscribed" name="do" type="radio" value="subscribed" />
                <h4>Watching</h4>
                <span class="description">You receive notifications for all conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-eye-unwatch"></span>
                  Unwatch
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

            <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <div class="select-menu-item-text">
                <input id="do_ignore" name="do" type="radio" value="ignore" />
                <h4>Ignoring</h4>
                <span class="description">You do not receive any notifications for conversations in this repository.</span>
                <span class="js-select-button-text hidden-select-button-text">
                  <span class="octicon octicon-mute"></span>
                  Stop ignoring
                </span>
              </div>
            </div> <!-- /.select-menu-item -->

          </div> <!-- /.select-menu-list -->

        </div> <!-- /.select-menu-modal -->
      </div> <!-- /.select-menu-modal-holder -->
    </div> <!-- /.select-menu -->

</form>
    </li>

  <li>
  

  <div class="js-toggler-container js-social-container starring-container ">
    <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/unstar"
      class="minibutton with-count js-toggler-target star-button starred upwards"
      title="Unstar this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star-delete"></span><span class="text">Unstar</span>
    </a>

    <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/star"
      class="minibutton with-count js-toggler-target star-button unstarred upwards"
      title="Star this repository" data-remote="true" data-method="post" rel="nofollow">
      <span class="octicon octicon-star"></span><span class="text">Star</span>
    </a>

      <a class="social-count js-social-count" href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/stargazers">
        0
      </a>
  </div>

  </li>


        <li>
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/fork" class="minibutton with-count js-toggler-target fork-button lighter upwards" title="Fork this repo" rel="nofollow" data-method="post">
            <span class="octicon octicon-git-branch-create"></span><span class="text">Fork</span>
          </a>
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/network" class="social-count">0</a>
        </li>


</ul>

        <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public">
          <span class="repo-label"><span>public</span></span>
          <span class="mega-octicon octicon-repo"></span>
          <span class="author">
            <a href="/biomystery" class="url fn" itemprop="url" rel="author"><span itemprop="title">biomystery</span></a>
          </span>
          <span class="repohead-name-divider">/</span>
          <strong><a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" class="js-current-repository js-repo-home-link">bioinformatics_algorithms1_coursera_2013_ucsd</a></strong>

          <span class="page-context-loader">
            <img alt="Octocat-spinner-32" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </span>

        </h1>
      </div><!-- /.container -->
    </div><!-- /.repohead -->

    <div class="container">
      

      <div class="repository-with-sidebar repo-container  ">

        <div class="repository-sidebar">
            

<div class="sunken-menu vertical-right repo-nav js-repo-nav js-repository-container-pjax js-octicon-loaders">
  <div class="sunken-menu-contents">
    <ul class="sunken-menu-group">
      <li class="tooltipped leftwards" title="Code">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" aria-label="Code" class="selected js-selected-navigation-item sunken-menu-item" data-gotokey="c" data-pjax="true" data-selected-links="repo_source repo_downloads repo_commits repo_tags repo_branches /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd">
          <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

        <li class="tooltipped leftwards" title="Issues">
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="i" data-selected-links="repo_issues /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/issues">
            <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>

      <li class="tooltipped leftwards" title="Pull Requests">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/pulls" aria-label="Pull Requests" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-gotokey="p" data-selected-links="repo_pulls /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/pulls">
            <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull Requests</span>
            <span class='counter'>0</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>


        <li class="tooltipped leftwards" title="Wiki">
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_wiki /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/wiki">
            <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>        </li>
    </ul>
    <div class="sunken-menu-separator"></div>
    <ul class="sunken-menu-group">

      <li class="tooltipped leftwards" title="Pulse">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="pulse /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/pulse">
          <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Graphs">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-pjax="true" data-selected-links="repo_graphs repo_contributors /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/graphs">
          <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

      <li class="tooltipped leftwards" title="Network">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/network" aria-label="Network" class="js-selected-navigation-item sunken-menu-item js-disable-pjax" data-selected-links="repo_network /biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/network">
          <span class="octicon octicon-git-branch"></span> <span class="full-word">Network</span>
          <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
    </ul>


      <div class="sunken-menu-separator"></div>
      <ul class="sunken-menu-group">
        <li class="tooltipped leftwards" title="Settings">
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/settings"
            class="sunken-menu-item" data-pjax aria-label="Settings">
            <span class="octicon octicon-tools"></span> <span class="full-word">Settings</span>
            <img alt="Octocat-spinner-32" class="mini-loader" height="16" src="https://github.global.ssl.fastly.net/images/spinners/octocat-spinner-32.gif" width="16" />
          </a>
        </li>
      </ul>
  </div>
</div>

            <div class="only-with-full-nav">
              

  

<div class="clone-url open"
  data-protocol-type="http"
  data-url="/users/set_protocol?protocol_selector=http&amp;protocol_type=push">
  <h3><strong>HTTPS</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="ssh"
  data-url="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=push">
  <h3><strong>SSH</strong> clone URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="git@github.com:biomystery/bioinformatics_algorithms1_coursera_2013_ucsd.git" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="git@github.com:biomystery/bioinformatics_algorithms1_coursera_2013_ucsd.git" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>

  

<div class="clone-url "
  data-protocol-type="subversion"
  data-url="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=push">
  <h3><strong>Subversion</strong> checkout URL</h3>
  <div class="clone-url-box">
    <input type="text" class="clone js-url-field"
           value="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" readonly="readonly">

    <span class="js-zeroclipboard url-box-clippy minibutton zeroclipboard-button" data-clipboard-text="https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>


<p class="clone-options">You can clone with
      <a href="#" class="js-clone-selector" data-protocol="http">HTTPS</a>,
      <a href="#" class="js-clone-selector" data-protocol="ssh">SSH</a>,
      or <a href="#" class="js-clone-selector" data-protocol="subversion">Subversion</a>.
  <span class="octicon help tooltipped upwards" title="Get help on which URL is right for you.">
    <a href="https://help.github.com/articles/which-remote-url-should-i-use">
    <span class="octicon octicon-question"></span>
    </a>
  </span>
</p>

  <a href="http://mac.github.com" data-url="github-mac://openRepo/https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" class="minibutton sidebar-button js-conduit-rewrite-url">
    <span class="octicon octicon-device-desktop"></span>
    Clone in Desktop
  </a>


              <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/archive/master.zip"
                 class="minibutton sidebar-button"
                 title="Download this repository as a zip file"
                 rel="nofollow">
                <span class="octicon octicon-cloud-download"></span>
                Download ZIP
              </a>
            </div>
        </div><!-- /.repository-sidebar -->

        <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>
          


<!-- blob contrib key: blob_contributors:v21:81ad7e8511c38d160794fa1e049c18f2 -->

<p title="This is a placeholder element" class="js-history-link-replace hidden"></p>

<a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/find/master" data-pjax data-hotkey="t" class="js-show-file-finder" style="display:none">Show File Finder</a>

<div class="file-navigation">
  

<div class="select-menu js-menu-container js-select-menu" >
  <span class="minibutton select-menu-button js-menu-target" data-hotkey="w"
    data-master-branch="master"
    data-ref="master"
    role="button" aria-label="Switch branches or tags" tabindex="0">
    <span class="octicon octicon-git-branch"></span>
    <i>branch:</i>
    <span class="js-select-button">master</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-remove-close js-menu-close"></span>
      </div> <!-- /.select-menu-header -->

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Find or create a branch…" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Find or create a branch…">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" class="js-select-menu-tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" class="js-select-menu-tab">Tags</a>
            </li>
          </ul>
        </div><!-- /.select-menu-tabs -->
      </div><!-- /.select-menu-filters -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <div class="select-menu-item js-navigation-item selected">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/blob/master/ch7/fittingAlignment.py"
                 data-name="master"
                 data-skip-pjax="true"
                 rel="nofollow"
                 class="js-navigation-open select-menu-item-text js-select-button-text css-truncate-target"
                 title="master">master</a>
            </div> <!-- /.select-menu-item -->
        </div>

          <form accept-charset="UTF-8" action="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/branches" class="js-create-branch select-menu-item select-menu-new-item-form js-navigation-item js-new-item-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="authenticity_token" type="hidden" value="7e4A2FbZl3W7x6MA2Xa5oAF37zPn0I6Wv2dzeJmilK4=" /></div>
            <span class="octicon octicon-git-branch-create select-menu-item-icon"></span>
            <div class="select-menu-item-text">
              <h4>Create branch: <span class="js-new-item-name"></span></h4>
              <span class="description">from ‘master’</span>
            </div>
            <input type="hidden" name="name" id="name" class="js-new-item-value">
            <input type="hidden" name="branch" id="branch" value="master" />
            <input type="hidden" name="path" id="path" value="ch7/fittingAlignment.py" />
          </form> <!-- /.select-menu-item -->

      </div> <!-- /.select-menu-list -->

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div> <!-- /.select-menu-list -->

    </div> <!-- /.select-menu-modal -->
  </div> <!-- /.select-menu-modal-holder -->
</div> <!-- /.select-menu -->

  <div class="breadcrumb">
    <span class='repo-root js-repo-root'><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">bioinformatics_algorithms1_coursera_2013_ucsd</span></a></span></span><span class="separator"> / </span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/tree/master/ch7" data-branch="master" data-direction="back" data-pjax="true" itemscope="url"><span itemprop="title">ch7</span></a></span><span class="separator"> / </span><strong class="final-path">fittingAlignment.py</strong> <span class="js-zeroclipboard minibutton zeroclipboard-button" data-clipboard-text="ch7/fittingAlignment.py" data-copied-hint="copied!" title="copy to clipboard"><span class="octicon octicon-clippy"></span></span>
  </div>
</div>



  <div class="commit file-history-tease">
    <img class="main-avatar" height="24" src="https://0.gravatar.com/avatar/a1574873074d962564e1436d308d0243?d=https%3A%2F%2Fidenticons.github.com%2F270a598bc10d96e5224988fd04ce3c14.png&amp;r=x&amp;s=140" width="24" />
    <span class="author"><a href="/biomystery" rel="author">biomystery</a></span>
    <time class="js-relative-date" datetime="2014-01-03T09:08:28-08:00" title="2014-01-03 09:08:28">January 03, 2014</time>
    <div class="commit-title">
        <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/commit/803cf0f27815bc6cad664d1ce62662c2c802fb91" class="message" data-pjax="true" title="fitting alignment

Bug: Too slow.">fitting alignment</a>
    </div>

    <div class="participation">
      <p class="quickstat"><a href="#blob_contributors_box" rel="facebox"><strong>1</strong> contributor</a></p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img height="24" src="https://0.gravatar.com/avatar/a1574873074d962564e1436d308d0243?d=https%3A%2F%2Fidenticons.github.com%2F270a598bc10d96e5224988fd04ce3c14.png&amp;r=x&amp;s=140" width="24" />
            <a href="/biomystery">biomystery</a>
          </li>
      </ul>
    </div>
  </div>

<div id="files" class="bubble">
  <div class="file">
    <div class="meta">
      <div class="info">
        <span class="icon"><b class="octicon octicon-file-text"></b></span>
        <span class="mode" title="File Mode">file</span>
          <span>82 lines (63 sloc)</span>
        <span>2.55 kb</span>
      </div>
      <div class="actions">
        <div class="button-group">
            <a class="minibutton tooltipped leftwards js-conduit-openfile-check"
               href="http://mac.github.com"
               data-url="github-mac://openRepo/https://github.com/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd?branch=master&amp;filepath=ch7%2FfittingAlignment.py"
               title="Open this file in GitHub for Mac"
               data-failed-title="Your version of GitHub for Mac is too old to open this file. Try checking for updates.">
                <span class="octicon octicon-device-desktop"></span> Open
            </a>
                <a class="minibutton"
                   href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/edit/master/ch7/fittingAlignment.py"
                   data-method="post" rel="nofollow" data-hotkey="e">Edit</a>
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/raw/master/ch7/fittingAlignment.py" class="button minibutton " id="raw-url">Raw</a>
            <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/blame/master/ch7/fittingAlignment.py" class="button minibutton ">Blame</a>
          <a href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/commits/master/ch7/fittingAlignment.py" class="button minibutton " rel="nofollow">History</a>
        </div><!-- /.button-group -->
          <a class="minibutton danger empty-icon tooltipped downwards"
             href="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/delete/master/ch7/fittingAlignment.py"
             title=""
             data-method="post" data-test-id="delete-blob-file" rel="nofollow">
          Delete
        </a>
      </div><!-- /.actions -->

    </div>
        <div class="blob-wrapper data type-python js-blob-data">
        <table class="file-code file-diff">
          <tr class="file-code-line">
            <td class="blob-line-nums">
              <span id="L1" rel="#L1">1</span>
<span id="L2" rel="#L2">2</span>
<span id="L3" rel="#L3">3</span>
<span id="L4" rel="#L4">4</span>
<span id="L5" rel="#L5">5</span>
<span id="L6" rel="#L6">6</span>
<span id="L7" rel="#L7">7</span>
<span id="L8" rel="#L8">8</span>
<span id="L9" rel="#L9">9</span>
<span id="L10" rel="#L10">10</span>
<span id="L11" rel="#L11">11</span>
<span id="L12" rel="#L12">12</span>
<span id="L13" rel="#L13">13</span>
<span id="L14" rel="#L14">14</span>
<span id="L15" rel="#L15">15</span>
<span id="L16" rel="#L16">16</span>
<span id="L17" rel="#L17">17</span>
<span id="L18" rel="#L18">18</span>
<span id="L19" rel="#L19">19</span>
<span id="L20" rel="#L20">20</span>
<span id="L21" rel="#L21">21</span>
<span id="L22" rel="#L22">22</span>
<span id="L23" rel="#L23">23</span>
<span id="L24" rel="#L24">24</span>
<span id="L25" rel="#L25">25</span>
<span id="L26" rel="#L26">26</span>
<span id="L27" rel="#L27">27</span>
<span id="L28" rel="#L28">28</span>
<span id="L29" rel="#L29">29</span>
<span id="L30" rel="#L30">30</span>
<span id="L31" rel="#L31">31</span>
<span id="L32" rel="#L32">32</span>
<span id="L33" rel="#L33">33</span>
<span id="L34" rel="#L34">34</span>
<span id="L35" rel="#L35">35</span>
<span id="L36" rel="#L36">36</span>
<span id="L37" rel="#L37">37</span>
<span id="L38" rel="#L38">38</span>
<span id="L39" rel="#L39">39</span>
<span id="L40" rel="#L40">40</span>
<span id="L41" rel="#L41">41</span>
<span id="L42" rel="#L42">42</span>
<span id="L43" rel="#L43">43</span>
<span id="L44" rel="#L44">44</span>
<span id="L45" rel="#L45">45</span>
<span id="L46" rel="#L46">46</span>
<span id="L47" rel="#L47">47</span>
<span id="L48" rel="#L48">48</span>
<span id="L49" rel="#L49">49</span>
<span id="L50" rel="#L50">50</span>
<span id="L51" rel="#L51">51</span>
<span id="L52" rel="#L52">52</span>
<span id="L53" rel="#L53">53</span>
<span id="L54" rel="#L54">54</span>
<span id="L55" rel="#L55">55</span>
<span id="L56" rel="#L56">56</span>
<span id="L57" rel="#L57">57</span>
<span id="L58" rel="#L58">58</span>
<span id="L59" rel="#L59">59</span>
<span id="L60" rel="#L60">60</span>
<span id="L61" rel="#L61">61</span>
<span id="L62" rel="#L62">62</span>
<span id="L63" rel="#L63">63</span>
<span id="L64" rel="#L64">64</span>
<span id="L65" rel="#L65">65</span>
<span id="L66" rel="#L66">66</span>
<span id="L67" rel="#L67">67</span>
<span id="L68" rel="#L68">68</span>
<span id="L69" rel="#L69">69</span>
<span id="L70" rel="#L70">70</span>
<span id="L71" rel="#L71">71</span>
<span id="L72" rel="#L72">72</span>
<span id="L73" rel="#L73">73</span>
<span id="L74" rel="#L74">74</span>
<span id="L75" rel="#L75">75</span>
<span id="L76" rel="#L76">76</span>
<span id="L77" rel="#L77">77</span>
<span id="L78" rel="#L78">78</span>
<span id="L79" rel="#L79">79</span>
<span id="L80" rel="#L80">80</span>
<span id="L81" rel="#L81">81</span>

            </td>
            <td class="blob-line-code">
                    <div class="code-body highlight"><pre><div class='line' id='LC1'><span class="kn">import</span> <span class="nn">globalAlign</span> <span class="kn">as</span> <span class="nn">ga</span></div><div class='line' id='LC2'><br/></div><div class='line' id='LC3'><span class="k">def</span> <span class="nf">fittingAlignment</span><span class="p">(</span><span class="n">v</span><span class="p">,</span><span class="n">w</span><span class="p">):</span></div><div class='line' id='LC4'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="sd">&#39;&#39;&#39;</span></div><div class='line' id='LC5'><span class="sd">    Fitting Alignment Problem: Construct a highest-scoring fitting</span></div><div class='line' id='LC6'><span class="sd">    alignment between two strings. </span></div><div class='line' id='LC7'><span class="sd">    </span></div><div class='line' id='LC8'><span class="sd">    Input: Two nucleotide strings v and w, where v has length at most</span></div><div class='line' id='LC9'><span class="sd">    1000 and w has length at most 100. </span></div><div class='line' id='LC10'><span class="sd">    </span></div><div class='line' id='LC11'><span class="sd">    Output: A highest-scoring fitting alignment between v and w. Use the</span></div><div class='line' id='LC12'><span class="sd">    simple scoring method in which matches count +1 and both the</span></div><div class='line' id='LC13'><span class="sd">    mismatch and indel penalties are 1. </span></div><div class='line' id='LC14'><br/></div><div class='line' id='LC15'><br/></div><div class='line' id='LC16'><span class="sd">    Sample Input:</span></div><div class='line' id='LC17'><span class="sd">    GTAGGCTTAAGGTTA</span></div><div class='line' id='LC18'><span class="sd">    TAGATA</span></div><div class='line' id='LC19'><span class="sd">    </span></div><div class='line' id='LC20'><span class="sd">    Sample Output:</span></div><div class='line' id='LC21'><span class="sd">    2</span></div><div class='line' id='LC22'><span class="sd">    TAGGCTTA</span></div><div class='line' id='LC23'><span class="sd">    TAGA--TA</span></div><div class='line' id='LC24'><br/></div><div class='line' id='LC25'><span class="sd">    &quot;Fitting&quot; w to v requires finding a substring v&#39; of v that</span></div><div class='line' id='LC26'><span class="sd">    maximizes an alignment score the global alignment score between v&#39;</span></div><div class='line' id='LC27'><span class="sd">    and w among all substrings of v. For example, the best global,</span></div><div class='line' id='LC28'><span class="sd">    local, and fitting alignments of v = GTAGGCTTAAGGTTA and w = TAGATA</span></div><div class='line' id='LC29'><span class="sd">    are shown below (with mismatch and indel penalties equal to 1). </span></div><div class='line' id='LC30'><br/></div><div class='line' id='LC31'><span class="sd">    Note that the optimal local alignment is not a valid fitting</span></div><div class='line' id='LC32'><span class="sd">    alignment. On the other hand, the score of the optimal global</span></div><div class='line' id='LC33'><span class="sd">    alignment (-3) is smaller than that of the best fitting alignment</span></div><div class='line' id='LC34'><span class="sd">    (+2). </span></div><div class='line' id='LC35'><span class="sd">    &#39;&#39;&#39;</span></div><div class='line' id='LC36'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">v_subs</span> <span class="o">=</span> <span class="n">getSubstring</span><span class="p">(</span><span class="n">v</span><span class="p">,</span><span class="n">w</span><span class="p">)</span></div><div class='line' id='LC37'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">sigma</span> <span class="o">=</span> <span class="mi">1</span></div><div class='line' id='LC38'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c">#results = map(lambda v_sub: ga.globalAlign(w,v_sub,sigma),v_subs)</span></div><div class='line' id='LC39'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best_score</span><span class="p">,</span> <span class="n">best_align</span>  <span class="o">=</span> <span class="o">-</span><span class="mi">555</span><span class="p">,</span> <span class="p">[]</span></div><div class='line' id='LC40'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">idx</span><span class="p">,</span> <span class="n">v_sub</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">v_subs</span><span class="p">):</span></div><div class='line' id='LC41'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">idx</span> <span class="o">%</span> <span class="mi">100</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span></div><div class='line' id='LC42'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">print</span> <span class="nb">str</span><span class="p">(</span><span class="n">idx</span><span class="p">)</span> <span class="o">+</span> <span class="s">&#39;/&#39;</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">v_subs</span><span class="p">))</span></div><div class='line' id='LC43'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">align_tmp</span><span class="p">,</span> <span class="n">score_tmp</span> <span class="o">=</span> <span class="n">ga</span><span class="o">.</span><span class="n">globalAlign</span><span class="p">(</span><span class="n">v_sub</span><span class="p">,</span><span class="n">w</span><span class="p">,</span><span class="n">sigma</span><span class="p">)</span></div><div class='line' id='LC44'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">if</span> <span class="n">score_tmp</span> <span class="o">&gt;</span> <span class="n">best_score</span><span class="p">:</span></div><div class='line' id='LC45'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best_score</span> <span class="o">=</span> <span class="n">score_tmp</span></div><div class='line' id='LC46'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">best_align</span> <span class="o">=</span> <span class="n">align_tmp</span></div><div class='line' id='LC47'><br/></div><div class='line' id='LC48'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="n">best_align</span><span class="p">,</span> <span class="n">best_score</span></div><div class='line' id='LC49'><br/></div><div class='line' id='LC50'><span class="c"># all substrings:</span></div><div class='line' id='LC51'><span class="c"># http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n</span></div><div class='line' id='LC52'><span class="c"># Thanks to Claudiu, recursive solution</span></div><div class='line' id='LC53'><span class="k">def</span> <span class="nf">subStringLen</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="n">length</span><span class="p">):</span></div><div class='line' id='LC54'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="p">[</span><span class="nb">str</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span><span class="o">+</span><span class="n">length</span><span class="p">]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="nb">str</span><span class="p">)</span><span class="o">-</span><span class="n">length</span><span class="o">+</span><span class="mi">1</span><span class="p">)]</span></div><div class='line' id='LC55'><br/></div><div class='line' id='LC56'><br/></div><div class='line' id='LC57'><span class="k">def</span> <span class="nf">getSubstring</span><span class="p">(</span><span class="n">v</span><span class="p">,</span><span class="n">w</span><span class="p">):</span></div><div class='line' id='LC58'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output</span> <span class="o">=</span> <span class="p">[]</span></div><div class='line' id='LC59'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">w</span><span class="p">),</span><span class="nb">int</span><span class="p">(</span><span class="mf">1.5</span><span class="o">*</span><span class="nb">len</span><span class="p">(</span><span class="n">w</span><span class="p">))</span><span class="o">+</span><span class="mi">1</span><span class="p">):</span></div><div class='line' id='LC60'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">output</span> <span class="o">+=</span> <span class="n">subStringLen</span><span class="p">(</span><span class="n">v</span><span class="p">,</span><span class="n">i</span><span class="p">)</span> </div><div class='line' id='LC61'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">output</span><span class="p">))</span></div><div class='line' id='LC62'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC63'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC64'><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&quot;__main__&quot;</span><span class="p">:</span></div><div class='line' id='LC65'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># read file and get parameters</span></div><div class='line' id='LC66'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s">&#39;fa_input.txt&#39;</span><span class="p">,</span><span class="s">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fin</span><span class="p">:</span></div><div class='line' id='LC67'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">v</span> <span class="o">=</span> <span class="n">fin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> </div><div class='line' id='LC68'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">w</span> <span class="o">=</span> <span class="n">fin</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span> </div><div class='line' id='LC69'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC70'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># run the function </span></div><div class='line' id='LC71'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">align</span><span class="p">,</span> <span class="n">score</span> <span class="o">=</span> <span class="n">fittingAlignment</span><span class="p">(</span><span class="n">v</span><span class="p">,</span><span class="n">w</span><span class="p">)</span></div><div class='line' id='LC72'>&nbsp;&nbsp;&nbsp;&nbsp;</div><div class='line' id='LC73'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="c"># output the results</span></div><div class='line' id='LC74'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="k">with</span>  <span class="nb">open</span><span class="p">(</span><span class="s">&#39;fa_output.txt&#39;</span><span class="p">,</span><span class="s">&#39;w&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fout</span><span class="p">:</span></div><div class='line' id='LC75'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fout</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="s">&quot;</span><span class="si">%d</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">score</span><span class="p">)</span></div><div class='line' id='LC76'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fout</span><span class="o">.</span><span class="n">write</span> <span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">align</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></div><div class='line' id='LC77'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">fout</span><span class="o">.</span><span class="n">write</span> <span class="p">(</span><span class="s">&quot;</span><span class="si">%s</span><span class="se">\n</span><span class="s">&quot;</span> <span class="o">%</span> <span class="n">align</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span></div><div class='line' id='LC78'><br/></div><div class='line' id='LC79'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="kn">from</span> <span class="nn">subprocess</span> <span class="kn">import</span> <span class="n">call</span></div><div class='line' id='LC80'>&nbsp;&nbsp;&nbsp;&nbsp;<span class="n">call</span><span class="p">([</span><span class="s">&quot;open&quot;</span><span class="p">,</span><span class="s">&quot;fa_output.txt&quot;</span><span class="p">])</span>        </div><div class='line' id='LC81'><br/></div></pre></div>
            </td>
          </tr>
        </table>
  </div>

  </div>
</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" class="js-jump-to-line" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <form accept-charset="UTF-8" class="js-jump-to-line-form">
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" autofocus>
    <button type="submit" class="button">Go</button>
  </form>
</div>

        </div>

      </div><!-- /.repo-container -->
      <div class="modal-backdrop"></div>
    </div><!-- /.container -->
  </div><!-- /.site -->


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer">
    <ul class="site-footer-links right">
      <li><a href="https://status.github.com/">Status</a></li>
      <li><a href="http://developer.github.com">API</a></li>
      <li><a href="http://training.github.com">Training</a></li>
      <li><a href="http://shop.github.com">Shop</a></li>
      <li><a href="/blog">Blog</a></li>
      <li><a href="/about">About</a></li>

    </ul>

    <a href="/">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
    </a>

    <ul class="site-footer-links">
      <li>&copy; 2014 <span title="0.03915s from github-fe117-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="/site/terms">Terms</a></li>
        <li><a href="/site/privacy">Privacy</a></li>
        <li><a href="/security">Security</a></li>
        <li><a href="/contact">Contact</a></li>
    </ul>
  </div><!-- /.site-footer -->
</div><!-- /.container -->


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-fullscreen-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="js-fullscreen-contents" placeholder="" data-suggester="fullscreen_suggester"></textarea>
          <div class="suggester-container">
              <div class="suggester fullscreen-suggester js-navigation-container" id="fullscreen_suggester"
                 data-url="/biomystery/bioinformatics_algorithms1_coursera_2013_ucsd/suggestions/commit">
              </div>
          </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped leftwards" title="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped leftwards"
      title="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-remove-close close ajax-error-dismiss"></a>
      Something went wrong with that request. Please try again.
    </div>

  </body>
</html>

