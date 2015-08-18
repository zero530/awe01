


<!DOCTYPE html>
<html lang="en" class="">
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# object: http://ogp.me/ns/object# article: http://ogp.me/ns/article# profile: http://ogp.me/ns/profile#">
    <meta charset='utf-8'>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="Content-Language" content="en">
    <meta name="viewport" content="width=1020">
    
    
    <title>awesome-python3-webapp/models.py at day-07 · michaelliao/awesome-python3-webapp</title>
    <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <link rel="apple-touch-icon" sizes="57x57" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/apple-touch-icon-114.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/apple-touch-icon-144.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/apple-touch-icon-144.png">
    <meta property="fb:app_id" content="1401488693436528">

      <meta content="@github" name="twitter:site" /><meta content="summary" name="twitter:card" /><meta content="michaelliao/awesome-python3-webapp" name="twitter:title" /><meta content="awesome-python3-webapp - 小白的Python入门教程实战篇：网站+iOS App源码" name="twitter:description" /><meta content="https://avatars2.githubusercontent.com/u/470058?v=3&amp;s=400" name="twitter:image:src" />
      <meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="https://avatars2.githubusercontent.com/u/470058?v=3&amp;s=400" property="og:image" /><meta content="michaelliao/awesome-python3-webapp" property="og:title" /><meta content="https://github.com/michaelliao/awesome-python3-webapp" property="og:url" /><meta content="awesome-python3-webapp - 小白的Python入门教程实战篇：网站+iOS App源码" property="og:description" />
      <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">
    <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">
    <link rel="assets" href="https://assets-cdn.github.com/">
    <link rel="web-socket" href="wss://live.github.com/_sockets/MTM4MjYxNjc6ZTAyNjViMDk0MTIxN2QwNDIyNTdkNTE1M2ZmOGYyNGE6OWVjNWRiNTVjNjliNWRjZWI5NjA3MmVlMGJmYmMwMWFmOGI1NjdjYzJjYmI2ODJiOTFhYzBkNGRhNWQxZjg4Mg==--42c2f21d486f041a0a8124024666acbc92ee9b32">
    <meta name="pjax-timeout" content="1000">
    <link rel="sudo-modal" href="/sessions/sudo_modal">

    <meta name="msapplication-TileImage" content="/windows-tile.png">
    <meta name="msapplication-TileColor" content="#ffffff">
    <meta name="selected-link" value="repo_source" data-pjax-transient>

        <meta name="google-analytics" content="UA-3769691-2">

    <meta content="collector.githubapp.com" name="octolytics-host" /><meta content="collector-cdn.github.com" name="octolytics-script-host" /><meta content="github" name="octolytics-app-id" /><meta content="0E72315F:3D43:4521194:55D365A5" name="octolytics-dimension-request_id" /><meta content="13826167" name="octolytics-actor-id" /><meta content="zero530" name="octolytics-actor-login" /><meta content="9edc2f394f00f083764e2c6ea0c7a359408849ee116130b6dd109c30f6a4ea1d" name="octolytics-actor-hash" />
    
    <meta content="Rails, view, blob#show" data-pjax-transient="true" name="analytics-event" />
    <meta class="js-ga-set" name="dimension1" content="Logged In">
      <meta class="js-ga-set" name="dimension4" content="Current repo nav">
    <meta name="is-dotcom" content="true">
        <meta name="hostname" content="github.com">
    <meta name="user-login" content="zero530">

      <link rel="icon" sizes="any" mask href="https://assets-cdn.github.com/pinned-octocat.svg">
      <meta name="theme-color" content="#4078c0">
      <link rel="icon" type="image/x-icon" href="https://assets-cdn.github.com/favicon.ico">

    <!-- </textarea> --><!-- '"` --><meta content="authenticity_token" name="csrf-param" />
<meta content="DgA+wSckI7MSyprl0AQyVHMmiYMHlATkiKPbbT7e1s0fRnYJFcI8Uiysb3b2mA8Exa1v8YRgjZcEQKMMUmIgSg==" name="csrf-token" />
    

    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github/index-ce6f4be3ac86c80d26386e89dab12306e2663d0673dbcecb4cee57b1dc3585cb.css" media="all" rel="stylesheet" />
    <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github2/index-f717e72e116159102ffa893caf9e0a3d2189464fceceb966e342e0799334a12a.css" media="all" rel="stylesheet" />
    
    


    <meta http-equiv="x-pjax-version" content="d737a96d0fde9198bd2f7b9c27790a3a">

      
  <meta name="description" content="awesome-python3-webapp - 小白的Python入门教程实战篇：网站+iOS App源码">
  <meta name="go-import" content="github.com/michaelliao/awesome-python3-webapp git https://github.com/michaelliao/awesome-python3-webapp.git">

  <meta content="470058" name="octolytics-dimension-user_id" /><meta content="michaelliao" name="octolytics-dimension-user_login" /><meta content="35976854" name="octolytics-dimension-repository_id" /><meta content="michaelliao/awesome-python3-webapp" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="35976854" name="octolytics-dimension-repository_network_root_id" /><meta content="michaelliao/awesome-python3-webapp" name="octolytics-dimension-repository_network_root_nwo" />
  <link href="https://github.com/michaelliao/awesome-python3-webapp/commits/day-07.atom" rel="alternate" title="Recent Commits to awesome-python3-webapp:day-07" type="application/atom+xml">

  </head>


  <body class="logged_in  env-production windows vis-public page-blob">
    <a href="#start-of-content" tabindex="1" class="accessibility-aid js-skip-to-content">Skip to content</a>
    <div class="wrapper">
      
      
      



        <div class="header header-logged-in true" role="banner">
  <div class="container clearfix">

    <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <span class="mega-octicon octicon-mark-github"></span>
</a>


      <div class="site-search repo-scope js-site-search" role="search">
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/search" class="js-site-search-form" data-global-search-url="/search" data-repo-search-url="/michaelliao/awesome-python3-webapp/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
  <label class="js-chromeless-input-container form-control">
    <div class="scope-badge">This repository</div>
    <input type="text"
      class="js-site-search-focus js-site-search-field is-clearable chromeless-input"
      data-hotkey="s"
      name="q"
      placeholder="Search"
      aria-label="Search this repository"
      data-global-scope-placeholder="Search GitHub"
      data-repo-scope-placeholder="Search"
      tabindex="1"
      autocapitalize="off">
  </label>
</form>
      </div>

      <ul class="header-nav left" role="navigation">
        <li class="header-nav-item">
          <a href="/pulls" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
            Pull requests
</a>        </li>
        <li class="header-nav-item">
          <a href="/issues" class="js-selected-navigation-item header-nav-link" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
            Issues
</a>        </li>
          <li class="header-nav-item">
            <a class="header-nav-link" href="https://gist.github.com/" data-ga-click="Header, go to gist, text:gist">Gist</a>
          </li>
      </ul>

    
<ul class="header-nav user-nav right" id="user-links">
  <li class="header-nav-item">
      <span class="js-socket-channel js-updatable-content"
        data-channel="notification-changed:zero530"
        data-url="/notifications/header">
      <a href="/notifications" aria-label="You have no unread notifications" class="header-nav-link notification-indicator tooltipped tooltipped-s" data-ga-click="Header, go to notifications, icon:read" data-hotkey="g n">
          <span class="mail-status all-read"></span>
          <span class="octicon octicon-inbox"></span>
</a>  </span>

  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link tooltipped tooltipped-s js-menu-target" href="/new"
       aria-label="Create new…"
       data-ga-click="Header, create new, icon:add">
      <span class="octicon octicon-plus left"></span>
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>


  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="michaelliao/awesome-python3-webapp">This repository</span>
  </div>
    <a class="dropdown-item" href="/michaelliao/awesome-python3-webapp/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </div>
  </li>

  <li class="header-nav-item dropdown js-menu-container">
    <a class="header-nav-link name tooltipped tooltipped-s js-menu-target" href="/zero530"
       aria-label="View profile and more"
       data-ga-click="Header, show menu, icon:avatar">
      <img alt="@zero530" class="avatar" height="20" src="https://avatars1.githubusercontent.com/u/13826167?v=3&amp;s=40" width="20" />
      <span class="dropdown-caret"></span>
    </a>

    <div class="dropdown-menu-content js-menu-content">
      <div class="dropdown-menu dropdown-menu-sw">
        <div class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">zero530</strong>
        </div>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/zero530" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a>
        <a class="dropdown-item" href="/stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a>
        <a class="dropdown-item" href="/explore" data-ga-click="Header, go to explore, text:explore">
          Explore
        </a>
        <a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a>
        <div class="dropdown-divider"></div>

        <a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a>

        <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/logout" class="logout-form" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="PnD4AKmrL0E15NGNUfKCw5JJlnvXsWLxBJVCmI2wXaOOu7BM/rw33XxFMZeyidtEDz4zLB+6Su+4PKbPLukA6g==" /></div>
          <button class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </li>
</ul>


    
  </div>
</div>

        

        


      <div id="start-of-content" class="accessibility-aid"></div>
          <div class="site" itemscope itemtype="http://schema.org/WebPage">
    <div id="js-flash-container">
      
    </div>
    <div class="pagehead repohead instapaper_ignore readability-menu ">
      <div class="container">

        <div class="clearfix">
          
<ul class="pagehead-actions">

  <li>
      <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="d1IhFRHDIUeR7ZfBdzKWsKc68Y3Ldy5ro/DxhbQ+X2iTAlLgagK4olgS9UTkWOM2QV6GnASW6CP60sBSt/Uq3w==" /></div>    <input id="repository_id" name="repository_id" type="hidden" value="35976854" />

      <div class="select-menu js-menu-container js-select-menu">
        <a href="/michaelliao/awesome-python3-webapp/subscription"
          class="btn btn-sm btn-with-count select-menu-button js-menu-target" role="button" tabindex="0" aria-haspopup="true"
          data-ga-click="Repository, click Watch settings, action:blob#show">
          <span class="js-select-button">
            <span class="octicon octicon-eye"></span>
            Watch
          </span>
        </a>
        <a class="social-count js-social-count" href="/michaelliao/awesome-python3-webapp/watchers">
          8
        </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content" aria-hidden="true">
            <div class="select-menu-header">
              <span class="select-menu-title">Notifications</span>
              <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
            </div>

            <div class="select-menu-list js-navigation-container" role="menu">

              <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                  <span class="select-menu-item-heading">Not watching</span>
                  <span class="description">Be notified when participating or @mentioned.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Watch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                  <span class="select-menu-item-heading">Watching</span>
                  <span class="description">Be notified of all conversations.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-eye"></span>
                    Unwatch
                  </span>
                </div>
              </div>

              <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                <span class="select-menu-item-icon octicon octicon-check"></span>
                <div class="select-menu-item-text">
                  <input id="do_ignore" name="do" type="radio" value="ignore" />
                  <span class="select-menu-item-heading">Ignoring</span>
                  <span class="description">Never be notified.</span>
                  <span class="js-select-button-text hidden-select-button-text">
                    <span class="octicon octicon-mute"></span>
                    Stop ignoring
                  </span>
                </div>
              </div>

            </div>

          </div>
        </div>
      </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">

    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/unstar" class="js-toggler-form starred js-unstar-button" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="I7v589O3jftoM+PzpEJqnIJ/AZFw18qmn2IfjqvrECLY0uogX2Jz7rXbKsupkqeYqRY+QGxWBTUokLCPbAb/fA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar michaelliao/awesome-python3-webapp"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <span class="octicon octicon-star"></span>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/michaelliao/awesome-python3-webapp/stargazers">
          23
        </a>
</form>
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/star" class="js-toggler-form unstarred js-star-button" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Vn1g7cqfbgFE3exMqBIxdSaJ8A9V/pzkBKjoWivYsq1if4zdPjpHyOIBjXLm8H2K0bgskWUBfBSfRJufkMQSjA==" /></div>
      <button
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star michaelliao/awesome-python3-webapp"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <span class="octicon octicon-star"></span>
        Star
      </button>
        <a class="social-count js-social-count" href="/michaelliao/awesome-python3-webapp/stargazers">
          23
        </a>
</form>  </div>

  </li>

        <li>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/fork" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="2BysCO+mnrkiQmk6rQNcYdY1g1QdGmKpLhqJZY2+OMLYSyeDoqkaU3yTz6zqO9PSVSCAoELm+zYWHh1aHDE2rg==" /></div>
            <button
                type="submit"
                class="btn btn-sm btn-with-count"
                data-ga-click="Repository, show fork modal, action:blob#show; text:Fork"
                title="Fork your own copy of michaelliao/awesome-python3-webapp to your account"
                aria-label="Fork your own copy of michaelliao/awesome-python3-webapp to your account">
              <span class="octicon octicon-repo-forked"></span>
              Fork
            </button>
            <a href="/michaelliao/awesome-python3-webapp/network" class="social-count">72</a>
</form>        </li>

</ul>

          <h1 itemscope itemtype="http://data-vocabulary.org/Breadcrumb" class="entry-title public ">
            <span class="mega-octicon octicon-repo"></span>
            <span class="author"><a href="/michaelliao" class="url fn" itemprop="url" rel="author"><span itemprop="title">michaelliao</span></a></span><!--
         --><span class="path-divider">/</span><!--
         --><strong><a href="/michaelliao/awesome-python3-webapp" data-pjax="#js-repo-pjax-container">awesome-python3-webapp</a></strong>

            <span class="page-context-loader">
              <img alt="" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
            </span>

          </h1>
        </div>

      </div>
    </div>

      <div class="container">
        <div class="repository-with-sidebar repo-container new-discussion-timeline ">
          <div class="repository-sidebar clearfix">
              

<nav class="sunken-menu repo-nav js-repo-nav js-sidenav-container-pjax js-octicon-loaders"
     role="navigation"
     data-pjax="#js-repo-pjax-container"
     data-issue-count-url="/michaelliao/awesome-python3-webapp/issues/counts">
  <ul class="sunken-menu-group">
    <li class="tooltipped tooltipped-w" aria-label="Code">
      <a href="/michaelliao/awesome-python3-webapp/tree/day-07" aria-label="Code" aria-selected="true" class="js-selected-navigation-item selected sunken-menu-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches /michaelliao/awesome-python3-webapp/tree/day-07">
        <span class="octicon octicon-code"></span> <span class="full-word">Code</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Issues">
        <a href="/michaelliao/awesome-python3-webapp/issues" aria-label="Issues" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /michaelliao/awesome-python3-webapp/issues">
          <span class="octicon octicon-issue-opened"></span> <span class="full-word">Issues</span>
          <span class="js-issue-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>

    <li class="tooltipped tooltipped-w" aria-label="Pull requests">
      <a href="/michaelliao/awesome-python3-webapp/pulls" aria-label="Pull requests" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g p" data-selected-links="repo_pulls /michaelliao/awesome-python3-webapp/pulls">
          <span class="octicon octicon-git-pull-request"></span> <span class="full-word">Pull requests</span>
          <span class="js-pull-replace-counter"></span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

      <li class="tooltipped tooltipped-w" aria-label="Wiki">
        <a href="/michaelliao/awesome-python3-webapp/wiki" aria-label="Wiki" class="js-selected-navigation-item sunken-menu-item" data-hotkey="g w" data-selected-links="repo_wiki /michaelliao/awesome-python3-webapp/wiki">
          <span class="octicon octicon-book"></span> <span class="full-word">Wiki</span>
          <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>      </li>
  </ul>
  <div class="sunken-menu-separator"></div>
  <ul class="sunken-menu-group">

    <li class="tooltipped tooltipped-w" aria-label="Pulse">
      <a href="/michaelliao/awesome-python3-webapp/pulse" aria-label="Pulse" class="js-selected-navigation-item sunken-menu-item" data-selected-links="pulse /michaelliao/awesome-python3-webapp/pulse">
        <span class="octicon octicon-pulse"></span> <span class="full-word">Pulse</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>

    <li class="tooltipped tooltipped-w" aria-label="Graphs">
      <a href="/michaelliao/awesome-python3-webapp/graphs" aria-label="Graphs" class="js-selected-navigation-item sunken-menu-item" data-selected-links="repo_graphs repo_contributors /michaelliao/awesome-python3-webapp/graphs">
        <span class="octicon octicon-graph"></span> <span class="full-word">Graphs</span>
        <img alt="" class="mini-loader" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32.gif" width="16" />
</a>    </li>
  </ul>


</nav>

                <div class="only-with-full-nav">
                    
<div class="js-clone-url clone-url open"
  data-protocol-type="http">
  <h3><span class="text-emphasized">HTTPS</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/michaelliao/awesome-python3-webapp.git" readonly="readonly" aria-label="HTTPS clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="ssh">
  <h3><span class="text-emphasized">SSH</span> clone URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="git@github.com:michaelliao/awesome-python3-webapp.git" readonly="readonly" aria-label="SSH clone URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>

  
<div class="js-clone-url clone-url "
  data-protocol-type="subversion">
  <h3><span class="text-emphasized">Subversion</span> checkout URL</h3>
  <div class="input-group js-zeroclipboard-container">
    <input type="text" class="input-mini input-monospace js-url-field js-zeroclipboard-target"
           value="https://github.com/michaelliao/awesome-python3-webapp" readonly="readonly" aria-label="Subversion checkout URL">
    <span class="input-group-button">
      <button aria-label="Copy to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </span>
  </div>
</div>



  <div class="clone-options">You can clone with
    <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=http&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="lf1ywrz8fAYUDAr8VlWNaD1+QAYUjb5rvoFgIlenpNAVI2/qYcqs4KaCjqLbER+kLYFNEbglmYqjVO9v+Yy67A==" /></div><button class="btn-link js-clone-selector" data-protocol="http" type="submit">HTTPS</button></form>, <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=ssh&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="hZWxzY0mfElHrtcYq+zgFnM7QySLjD90twiTSeQ9hXOsY+z8lluvoj2Cn+lDHz2/HrcYG2UsmXU8xGY2RD4EXg==" /></div><button class="btn-link js-clone-selector" data-protocol="ssh" type="submit">SSH</button></form>, or <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/users/set_protocol?protocol_selector=subversion&amp;protocol_type=clone" class="inline-form js-clone-selector-form is-enabled" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="/dd5kDUjB1cxajSErVEcZx/i/zV8OnJWaU/ZIjmxLy31WYP2QFxktpsF9VnyXkesa/+85ZWmRUe326HSxfXI6Q==" /></div><button class="btn-link js-clone-selector" data-protocol="subversion" type="submit">Subversion</button></form>.
    <a href="https://help.github.com/articles/which-remote-url-should-i-use" class="help tooltipped tooltipped-n" aria-label="Get help on which URL is right for you.">
      <span class="octicon octicon-question"></span>
    </a>
  </div>
    <a href="https://windows.github.com" class="btn btn-sm sidebar-button" title="Save michaelliao/awesome-python3-webapp to your computer and use it in GitHub Desktop." aria-label="Save michaelliao/awesome-python3-webapp to your computer and use it in GitHub Desktop.">
      <span class="octicon octicon-desktop-download"></span>
      Clone in Desktop
    </a>

                  <a href="/michaelliao/awesome-python3-webapp/archive/day-07.zip"
                     class="btn btn-sm sidebar-button"
                     aria-label="Download the contents of michaelliao/awesome-python3-webapp as a zip file"
                     title="Download the contents of michaelliao/awesome-python3-webapp as a zip file"
                     rel="nofollow">
                    <span class="octicon octicon-cloud-download"></span>
                    Download ZIP
                  </a>
                </div>
          </div>
          <div id="js-repo-pjax-container" class="repository-content context-loader-container" data-pjax-container>

            

<a href="/michaelliao/awesome-python3-webapp/blob/e6a66c155056aaf952d4d20ca3e1003dfdc4b875/www/models.py" class="hidden js-permalink-shortcut" data-hotkey="y">Permalink</a>

<!-- blob contrib key: blob_contributors:v21:a41df090cf89b617f4ff699838419afb -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu js-menu-container js-select-menu left">
  <span class="btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    data-ref="day-07"
    title="day-07"
    role="button" aria-label="Switch branches or tags" tabindex="0" aria-haspopup="true">
    <i>Branch:</i>
    <span class="js-select-button css-truncate-target">day-07</span>
  </span>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax aria-hidden="true">

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <span class="select-menu-title">Switch branches/tags</span>
        <span class="octicon octicon-x js-menu-close" role="button" aria-label="Close"></span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-01/www/models.py"
               data-name="day-01"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-01">
                day-01
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-02/www/models.py"
               data-name="day-02"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-02">
                day-02
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-03/www/models.py"
               data-name="day-03"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-03">
                day-03
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-04/www/models.py"
               data-name="day-04"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-04">
                day-04
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-05/www/models.py"
               data-name="day-05"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-05">
                day-05
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-06/www/models.py"
               data-name="day-06"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-06">
                day-06
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/michaelliao/awesome-python3-webapp/blob/day-07/www/models.py"
               data-name="day-07"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-07">
                day-07
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-08/www/models.py"
               data-name="day-08"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-08">
                day-08
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-09/www/models.py"
               data-name="day-09"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-09">
                day-09
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-10/www/models.py"
               data-name="day-10"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-10">
                day-10
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-11/www/models.py"
               data-name="day-11"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-11">
                day-11
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-12/www/models.py"
               data-name="day-12"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-12">
                day-12
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-13/www/models.py"
               data-name="day-13"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-13">
                day-13
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-14/www/models.py"
               data-name="day-14"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-14">
                day-14
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-15/www/models.py"
               data-name="day-15"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-15">
                day-15
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/day-16/www/models.py"
               data-name="day-16"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="day-16">
                day-16
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/dev/www/models.py"
               data-name="dev"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="dev">
                dev
              </span>
            </a>
            <a class="select-menu-item js-navigation-item js-navigation-open "
               href="/michaelliao/awesome-python3-webapp/blob/master/www/models.py"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <span class="select-menu-item-icon octicon octicon-check"></span>
              <span class="select-menu-item-text css-truncate-target" title="master">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="btn-group right">
      <a href="/michaelliao/awesome-python3-webapp/find/day-07"
            class="js-show-file-finder btn btn-sm empty-icon tooltipped tooltipped-nw"
            data-pjax
            data-hotkey="t"
            aria-label="Quickly jump between files">
        <span class="octicon octicon-list-unordered"></span>
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm zeroclipboard-button tooltipped tooltipped-s" data-copied-hint="Copied!" type="button"><span class="octicon octicon-clippy"></span></button>
    </div>

    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/michaelliao/awesome-python3-webapp/tree/day-07" class="" data-branch="day-07" data-pjax="true" itemscope="url"><span itemprop="title">awesome-python3-webapp</span></a></span></span><span class="separator">/</span><span itemscope="" itemtype="http://data-vocabulary.org/Breadcrumb"><a href="/michaelliao/awesome-python3-webapp/tree/day-07/www" class="" data-branch="day-07" data-pjax="true" itemscope="url"><span itemprop="title">www</span></a></span><span class="separator">/</span><strong class="final-path">models.py</strong>
    </div>
  </div>


  <div class="commit file-history-tease">
    <div class="file-history-tease-header">
        <img alt="@michaelliao" class="avatar" height="24" src="https://avatars3.githubusercontent.com/u/470058?v=3&amp;s=48" width="24" />
        <span class="author"><a href="/michaelliao" rel="author">michaelliao</a></span>
        <time datetime="2015-05-20T22:42:12Z" is="relative-time">May 21, 2015</time>
        <div class="commit-title">
            <a href="/michaelliao/awesome-python3-webapp/commit/61ae41e583655b01c4ae549a2457121b6c0f1b21" class="message" data-pjax="true" title="add initial resource">add initial resource</a>
        </div>
    </div>

    <div class="participation">
      <p class="quickstat">
        <a href="#blob_contributors_box" rel="facebox">
          <strong>1</strong>
           contributor
        </a>
      </p>
      
    </div>
    <div id="blob_contributors_box" style="display:none">
      <h2 class="facebox-header">Users who have contributed to this file</h2>
      <ul class="facebox-user-list">
          <li class="facebox-user-list-item">
            <img alt="@michaelliao" height="24" src="https://avatars3.githubusercontent.com/u/470058?v=3&amp;s=48" width="24" />
            <a href="/michaelliao">michaelliao</a>
          </li>
      </ul>
    </div>
  </div>

<div class="file">
  <div class="file-header">
    <div class="file-actions">

      <div class="btn-group">
        <a href="/michaelliao/awesome-python3-webapp/raw/day-07/www/models.py" class="btn btn-sm " id="raw-url">Raw</a>
          <a href="/michaelliao/awesome-python3-webapp/blame/day-07/www/models.py" class="btn btn-sm js-update-url-with-hash">Blame</a>
        <a href="/michaelliao/awesome-python3-webapp/commits/day-07/www/models.py" class="btn btn-sm " rel="nofollow">History</a>
      </div>

        <a class="octicon-btn tooltipped tooltipped-nw"
           href="https://windows.github.com"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <span class="octicon octicon-desktop-download"></span>
        </a>

            <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/edit/day-07/www/models.py" class="inline-form" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="RdN4lTtEFnQX+C5SzFVO3sfGKc5T8XEWg8jLW4ICOukrQTlgusWa40RgpUwRO2LfrqvLT4JI/8QRD9htdnytzA==" /></div>
              <button class="octicon-btn tooltipped tooltipped-n" type="submit" aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
                <span class="octicon octicon-pencil"></span>
              </button>
</form>
          <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="/michaelliao/awesome-python3-webapp/delete/day-07/www/models.py" class="inline-form" data-form-nonce="637dad12455337e50c956bb114701e2b8064185f" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="Tn8Mn5cU/Fiw17q2mIUJgrUwlFJgpye0gkHPyvsrnJ2xRor4lRqFfQU5+yqzoCUVI8PlJadT0wW5p+bct0jczw==" /></div>
            <button class="octicon-btn octicon-btn-danger tooltipped tooltipped-n" type="submit" aria-label="Fork this project and delete this file" data-disable-with>
              <span class="octicon octicon-trashcan"></span>
            </button>
</form>    </div>

    <div class="file-info">
        50 lines (38 sloc)
        <span class="file-info-divider"></span>
      1.469 kB
    </div>
  </div>
  

  <div class="blob-wrapper data type-python">
      <table class="highlight tab-size js-file-line-container" data-tab-size="8">
      <tr>
        <td id="L1" class="blob-num js-line-number" data-line-number="1"></td>
        <td id="LC1" class="blob-code blob-code-inner js-file-line"><span class="pl-c">#!/usr/bin/env python3</span></td>
      </tr>
      <tr>
        <td id="L2" class="blob-num js-line-number" data-line-number="2"></td>
        <td id="LC2" class="blob-code blob-code-inner js-file-line"><span class="pl-c"># -*- coding: utf-8 -*-</span></td>
      </tr>
      <tr>
        <td id="L3" class="blob-num js-line-number" data-line-number="3"></td>
        <td id="LC3" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L4" class="blob-num js-line-number" data-line-number="4"></td>
        <td id="LC4" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L5" class="blob-num js-line-number" data-line-number="5"></td>
        <td id="LC5" class="blob-code blob-code-inner js-file-line"><span class="pl-s">Models for user, blog, comment.</span></td>
      </tr>
      <tr>
        <td id="L6" class="blob-num js-line-number" data-line-number="6"></td>
        <td id="LC6" class="blob-code blob-code-inner js-file-line"><span class="pl-s"><span class="pl-pds">&#39;&#39;&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L7" class="blob-num js-line-number" data-line-number="7"></td>
        <td id="LC7" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L8" class="blob-num js-line-number" data-line-number="8"></td>
        <td id="LC8" class="blob-code blob-code-inner js-file-line">__author__ <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>Michael Liao<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L9" class="blob-num js-line-number" data-line-number="9"></td>
        <td id="LC9" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L10" class="blob-num js-line-number" data-line-number="10"></td>
        <td id="LC10" class="blob-code blob-code-inner js-file-line"><span class="pl-k">import</span> time, uuid</td>
      </tr>
      <tr>
        <td id="L11" class="blob-num js-line-number" data-line-number="11"></td>
        <td id="LC11" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L12" class="blob-num js-line-number" data-line-number="12"></td>
        <td id="LC12" class="blob-code blob-code-inner js-file-line"><span class="pl-k">from</span> orm <span class="pl-k">import</span> Model, StringField, BooleanField, FloatField, TextField</td>
      </tr>
      <tr>
        <td id="L13" class="blob-num js-line-number" data-line-number="13"></td>
        <td id="LC13" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L14" class="blob-num js-line-number" data-line-number="14"></td>
        <td id="LC14" class="blob-code blob-code-inner js-file-line"><span class="pl-k">def</span> <span class="pl-en">next_id</span>():</td>
      </tr>
      <tr>
        <td id="L15" class="blob-num js-line-number" data-line-number="15"></td>
        <td id="LC15" class="blob-code blob-code-inner js-file-line">    <span class="pl-k">return</span> <span class="pl-s"><span class="pl-pds">&#39;</span><span class="pl-c1">%015d%s</span>000<span class="pl-pds">&#39;</span></span> <span class="pl-k">%</span> (<span class="pl-c1">int</span>(time.time() <span class="pl-k">*</span> <span class="pl-c1">1000</span>), uuid.uuid4().hex)</td>
      </tr>
      <tr>
        <td id="L16" class="blob-num js-line-number" data-line-number="16"></td>
        <td id="LC16" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L17" class="blob-num js-line-number" data-line-number="17"></td>
        <td id="LC17" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">User</span>(<span class="pl-e">Model</span>):</td>
      </tr>
      <tr>
        <td id="L18" class="blob-num js-line-number" data-line-number="18"></td>
        <td id="LC18" class="blob-code blob-code-inner js-file-line">    __table__ <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>users<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L19" class="blob-num js-line-number" data-line-number="19"></td>
        <td id="LC19" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L20" class="blob-num js-line-number" data-line-number="20"></td>
        <td id="LC20" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">id</span> <span class="pl-k">=</span> StringField(<span class="pl-smi">primary_key</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">default</span><span class="pl-k">=</span>next_id, <span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L21" class="blob-num js-line-number" data-line-number="21"></td>
        <td id="LC21" class="blob-code blob-code-inner js-file-line">    email <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L22" class="blob-num js-line-number" data-line-number="22"></td>
        <td id="LC22" class="blob-code blob-code-inner js-file-line">    passwd <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L23" class="blob-num js-line-number" data-line-number="23"></td>
        <td id="LC23" class="blob-code blob-code-inner js-file-line">    admin <span class="pl-k">=</span> BooleanField()</td>
      </tr>
      <tr>
        <td id="L24" class="blob-num js-line-number" data-line-number="24"></td>
        <td id="LC24" class="blob-code blob-code-inner js-file-line">    name <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L25" class="blob-num js-line-number" data-line-number="25"></td>
        <td id="LC25" class="blob-code blob-code-inner js-file-line">    image <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(500)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L26" class="blob-num js-line-number" data-line-number="26"></td>
        <td id="LC26" class="blob-code blob-code-inner js-file-line">    created_at <span class="pl-k">=</span> FloatField(<span class="pl-smi">default</span><span class="pl-k">=</span>time.time)</td>
      </tr>
      <tr>
        <td id="L27" class="blob-num js-line-number" data-line-number="27"></td>
        <td id="LC27" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L28" class="blob-num js-line-number" data-line-number="28"></td>
        <td id="LC28" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Blog</span>(<span class="pl-e">Model</span>):</td>
      </tr>
      <tr>
        <td id="L29" class="blob-num js-line-number" data-line-number="29"></td>
        <td id="LC29" class="blob-code blob-code-inner js-file-line">    __table__ <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>blogs<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L30" class="blob-num js-line-number" data-line-number="30"></td>
        <td id="LC30" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L31" class="blob-num js-line-number" data-line-number="31"></td>
        <td id="LC31" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">id</span> <span class="pl-k">=</span> StringField(<span class="pl-smi">primary_key</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">default</span><span class="pl-k">=</span>next_id, <span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L32" class="blob-num js-line-number" data-line-number="32"></td>
        <td id="LC32" class="blob-code blob-code-inner js-file-line">    user_id <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L33" class="blob-num js-line-number" data-line-number="33"></td>
        <td id="LC33" class="blob-code blob-code-inner js-file-line">    user_name <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L34" class="blob-num js-line-number" data-line-number="34"></td>
        <td id="LC34" class="blob-code blob-code-inner js-file-line">    user_image <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(500)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L35" class="blob-num js-line-number" data-line-number="35"></td>
        <td id="LC35" class="blob-code blob-code-inner js-file-line">    name <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L36" class="blob-num js-line-number" data-line-number="36"></td>
        <td id="LC36" class="blob-code blob-code-inner js-file-line">    summary <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(200)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L37" class="blob-num js-line-number" data-line-number="37"></td>
        <td id="LC37" class="blob-code blob-code-inner js-file-line">    content <span class="pl-k">=</span> TextField()</td>
      </tr>
      <tr>
        <td id="L38" class="blob-num js-line-number" data-line-number="38"></td>
        <td id="LC38" class="blob-code blob-code-inner js-file-line">    created_at <span class="pl-k">=</span> FloatField(<span class="pl-smi">default</span><span class="pl-k">=</span>time.time)</td>
      </tr>
      <tr>
        <td id="L39" class="blob-num js-line-number" data-line-number="39"></td>
        <td id="LC39" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L40" class="blob-num js-line-number" data-line-number="40"></td>
        <td id="LC40" class="blob-code blob-code-inner js-file-line"><span class="pl-k">class</span> <span class="pl-en">Comment</span>(<span class="pl-e">Model</span>):</td>
      </tr>
      <tr>
        <td id="L41" class="blob-num js-line-number" data-line-number="41"></td>
        <td id="LC41" class="blob-code blob-code-inner js-file-line">    __table__ <span class="pl-k">=</span> <span class="pl-s"><span class="pl-pds">&#39;</span>comments<span class="pl-pds">&#39;</span></span></td>
      </tr>
      <tr>
        <td id="L42" class="blob-num js-line-number" data-line-number="42"></td>
        <td id="LC42" class="blob-code blob-code-inner js-file-line">
</td>
      </tr>
      <tr>
        <td id="L43" class="blob-num js-line-number" data-line-number="43"></td>
        <td id="LC43" class="blob-code blob-code-inner js-file-line">    <span class="pl-c1">id</span> <span class="pl-k">=</span> StringField(<span class="pl-smi">primary_key</span><span class="pl-k">=</span><span class="pl-c1">True</span>, <span class="pl-smi">default</span><span class="pl-k">=</span>next_id, <span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L44" class="blob-num js-line-number" data-line-number="44"></td>
        <td id="LC44" class="blob-code blob-code-inner js-file-line">    blog_id <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L45" class="blob-num js-line-number" data-line-number="45"></td>
        <td id="LC45" class="blob-code blob-code-inner js-file-line">    user_id <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L46" class="blob-num js-line-number" data-line-number="46"></td>
        <td id="LC46" class="blob-code blob-code-inner js-file-line">    user_name <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(50)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L47" class="blob-num js-line-number" data-line-number="47"></td>
        <td id="LC47" class="blob-code blob-code-inner js-file-line">    user_image <span class="pl-k">=</span> StringField(<span class="pl-smi">ddl</span><span class="pl-k">=</span><span class="pl-s"><span class="pl-pds">&#39;</span>varchar(500)<span class="pl-pds">&#39;</span></span>)</td>
      </tr>
      <tr>
        <td id="L48" class="blob-num js-line-number" data-line-number="48"></td>
        <td id="LC48" class="blob-code blob-code-inner js-file-line">    content <span class="pl-k">=</span> TextField()</td>
      </tr>
      <tr>
        <td id="L49" class="blob-num js-line-number" data-line-number="49"></td>
        <td id="LC49" class="blob-code blob-code-inner js-file-line">    created_at <span class="pl-k">=</span> FloatField(<span class="pl-smi">default</span><span class="pl-k">=</span>time.time)</td>
      </tr>
</table>

  </div>

</div>

<a href="#jump-to-line" rel="facebox[.linejump]" data-hotkey="l" style="display:none">Jump to Line</a>
<div id="jump-to-line" style="display:none">
  <!-- </textarea> --><!-- '"` --><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <input class="linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
    <button type="submit" class="btn">Go</button>
</form></div>

          </div>
        </div>
        <div class="modal-backdrop"></div>
      </div>
  </div>


    </div><!-- /.wrapper -->

      <div class="container">
  <div class="site-footer" role="contentinfo">
    <ul class="site-footer-links right">
        <li><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
      <li><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>

    </ul>

    <a href="https://github.com" aria-label="Homepage">
      <span class="mega-octicon octicon-mark-github" title="GitHub"></span>
</a>
    <ul class="site-footer-links">
      <li>&copy; 2015 <span title="0.08521s from github-fe141-cp1-prd.iad.github.net">GitHub</span>, Inc.</li>
        <li><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact</a></li>
    </ul>
  </div>
</div>


    <div class="fullscreen-overlay js-fullscreen-overlay" id="fullscreen_overlay">
  <div class="fullscreen-container js-suggester-container">
    <div class="textarea-wrap">
      <textarea name="fullscreen-contents" id="fullscreen-contents" class="fullscreen-contents js-fullscreen-contents" placeholder="" aria-label=""></textarea>
      <div class="suggester-container">
        <div class="suggester fullscreen-suggester js-suggester js-navigation-container"></div>
      </div>
    </div>
  </div>
  <div class="fullscreen-sidebar">
    <a href="#" class="exit-fullscreen js-exit-fullscreen tooltipped tooltipped-w" aria-label="Exit Zen Mode">
      <span class="mega-octicon octicon-screen-normal"></span>
    </a>
    <a href="#" class="theme-switcher js-theme-switcher tooltipped tooltipped-w"
      aria-label="Switch themes">
      <span class="octicon octicon-color-mode"></span>
    </a>
  </div>
</div>



    
    

    <div id="ajax-error-message" class="flash flash-error">
      <span class="octicon octicon-alert"></span>
      <a href="#" class="octicon octicon-x flash-close js-ajax-error-dismiss" aria-label="Dismiss error"></a>
      Something went wrong with that request. Please try again.
    </div>


      <script crossorigin="anonymous" src="https://assets-cdn.github.com/assets/frameworks-b8bb6ec61f9699575b20bf19ef0781a267528db51d66151c51d5ec2717341fd8.js"></script>
      <script async="async" crossorigin="anonymous" src="https://assets-cdn.github.com/assets/github/index-dcf222e83264dd93dcd4a27e0629febc4727a10bc5a6740dc7da9d429dc473ec.js"></script>
      
      
    <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner hidden">
      <span class="octicon octicon-alert"></span>
      <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
      <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
    </div>
  </body>
</html>

