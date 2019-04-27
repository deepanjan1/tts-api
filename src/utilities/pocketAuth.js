// Grabs access token and saves it to state

import { Linking } from 'react-native';
import { POCKET_KEY } from '../../config';

const redirectUri = 'redirect_uri=' + 'TextToSpeech://authorizationFinished';

const getPermissions = () => {
  // Request token URL construction
  const issuerRequest = 'https://getpocket.com/v3/oauth/request?';
  const consumerKey = 'consumer_key=' + POCKET_KEY;
  const urlString = issuerRequest + '&' + consumerKey + '&' + redirectUri;

  // fetch response
  fetch(urlString)
  .then((response) => response.text())
  .then((res) => res)
  .then(async (requestToken) => {
    console.log({ requestToken });

    // authorize request token
    const requestAuth = 'https://getpocket.com/auth/authorize?';
    const urlStringAccess = requestAuth +
    requestToken.replace('code=', 'request_token=') + '&' + redirectUri;
    Linking.openURL(urlStringAccess);
    Linking.addEventListener('url', (responseUrl) => {
      console.log(responseUrl);
    });

    // console.log({response});
    return requestToken;
  })
  .then((response) => {
    // Access token URL construction
    const issuerAccess = 'https://getpocket.com/v3/oauth/authorize?';
    const urlStringAccess = issuerAccess + response + '&' + consumerKey;
    return fetch(urlStringAccess);
  })
  .then((resA) => console.log(resA))
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
