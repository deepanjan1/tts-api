// Grabs access token and saves it to state

import { POCKET_KEY } from '../../globalVariables.js';

const redirectUri = 'redirect_uri=' + 'TextToSpeech://';

const getPermissions = () => {
  // Request token URL construction
  const issuerRequest = 'https://getpocket.com/v3/oauth/request?';
  const consumerKey = 'consumer_key=' + POCKET_KEY;
  const urlString = issuerRequest + '&' + consumerKey + '&' + redirectUri;

  // fetch response
  fetch(urlString)
  .then((response) => response.text())
  .then((res) => res)
  .then((requestToken) => {
    console.log({ requestToken });

    // Access token URL construction
    const issuerAccess = 'https://getpocket.com/v3/oauth/authorize?';
    const urlStringAccess = issuerAccess + requestToken + '&' + consumerKey;
    return fetch(urlStringAccess);
  })
  .then((responseAccess) => responseAccess.text())
  .then((resA) => resA)
  .catch((error) => {
    console.error(error);});
};

// const getAccessToken = (requestToken) => {
//   // Access token URL construction
//   const issuerAccess = 'https://getpocket.com/auth/authorize?';
//
//   // var requestToken = await getRequestToken();
//
//   // .then((response) => response.replace('code=', 'request_token='));
//
//   const redirectUri = 'redirect_uri=' + 'TextToSpeech://';
//
//   const urlString = issuerAccess + requestToken + '&' + redirectUri;
//
//   fetch(urlString)
//   .then((response) => (response.text()))
//   .then((res) => res)
//   .catch((error) => {
//       console.error(error);
//     });
// };

export const authorizePocket = () => getPermissions();
