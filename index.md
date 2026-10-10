---
layout: page
title: LOTTunnels
---

<script async src="https://www.googletagmanager.com/gtag/js?id=UA-133649096-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'UA-133649096-1');
</script>

<div class="home-hero">
  <a href="https://github.com/LOTTunnels/LOTTunnels.github.io/blob/master/README.md">
    <img src="{{ '/assets/logo.png' | relative_url }}" alt="{{site.title}} Logo">
  </a>
  <div>
    <h2>Living Off The Tunnels</h2>
    <p>LOTTunnels is a community-driven project documenting digital tunneling tools and how they can be abused for data exfiltration, persistence, and shell access.</p>
    <nav class="home-actions" aria-label="Explore LOTTunnels">
      <a href="#binary-directory">Browse the catalog</a>
      <a href="{{ '/contributors/' | relative_url }}">Meet the contributors</a>
      <a href="https://lottunnels.github.io/domains.csv">Domains CSV</a>
      <a href="https://lottunnels.github.io/binaries.csv">Binaries CSV</a>
    </nav>
  </div>
</div>

<p class="home-note">Inspired by the <a href="https://lolbas-project.github.io/">LOLBAS project</a>. Thank you to everyone who contributes to the community.</p>

<section class="usage-section" aria-labelledby="usage-heading">
  <h2 id="usage-heading">Projects using LOTTunnels</h2>
  <p>Examples of projects and community posts featuring LOTTunnels.</p>
  <div class="usage-cards">
    <a class="usage-card" href="https://github.com/jeffreytigch/PreventKit" target="_blank" rel="noopener noreferrer">
      <span class="usage-source">GitHub project</span>
      <strong>PreventKit</strong>
      <span>Explore the project on GitHub</span>
    </a>
    <a class="usage-card" href="https://lnkd.in/p/dc8_H4Gy" target="_blank" rel="noopener noreferrer">
      <span class="usage-source">Community post</span>
      <strong>LOTTunnels on LinkedIn</strong>
      <span>View the LinkedIn post</span>
    </a>
  </div>
</section>

[functions]: /functions/
<section id="binary-directory" aria-label="Binary catalog">
<h2>Explore the catalog</h2>
<p>Search binaries by name, function, or type.</p>
{% include bin_table.html %}
</section>
