async function startProfile(profileIndex) {
  try {
    const profileId = profiles[profileIndex][1];
    const response = await fetch(`http://localhost:3001/v1.0/browser_profiles/${profileId}/start?automation=1`);
    const data = await response.json();

    const { port, wsEndpoint } = data.automation;
    profiles[profileIndex][2] = `ws://localhost:${port}${wsEndpoint}`; // add wsUrl to the profile's line
    fs.writeFileSync('profiles_dolphin_common.txt', profiles.map(profile => profile.join(';')).join('\n'));

    console.log(`Profile ${profiles[profileIndex][0]} started successfully with wsUrl: ${profiles[profileIndex][2]}`);
    
    const browser = await puppeteer.connect({
      browserWSEndpoint: profiles[profileIndex][2],
      defaultViewport: null
    });
