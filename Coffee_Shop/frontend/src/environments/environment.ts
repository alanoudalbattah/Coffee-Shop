/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */
var domain = 'fsnd-class.us.auth0.com'
var audience = 'CoffeeShop'
var clientId = 'kC6XtqLFIpQxQq5snGiqbKUNEEEGkgTA'
var callbackURL = 'https://127.0.0.1:8100'

export const environment = {
  production: false,
  apiServerUrl: 'http://127.0.0.1:5000', // the running FLASK api server url
  auth0: {
    url: 'https://'+domain+'/authorize?audience='+audience+'&response_type=token&client_id='+clientId+'&redirect_uri='+callbackURL, // the auth0 domain prefix
    audience: audience, // the audience set for the auth0 app
    clientId: clientId, // the client id generated for the auth0 app
    callbackURL: callbackURL, // the base url of the running ionic application. 
  }
};
