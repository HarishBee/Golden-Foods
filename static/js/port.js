
var __aps = [];

(function () {
    // Quick read cookie value
    function getCookieValue(a) {
        var b = document.cookie.match('(^|;)\\s*' + a + '\\s*=\\s*([^;]+)');
        return b ? parseFloat(b.pop()) : '';
    }
    // Configuration portion
    var EXP_COOKIE_NAME = 'experimentationVariation';
    var EXPIRATION_IN_DAYS = 180; // 6 months
    var email = '';
    var isTestcafe = false;
    window.__brandName__ = 'grubhub';
    try {
        email = JSON.parse(localStorage.getItem('ngStorage-account')).email;
        isTestcafe = localStorage.getItem('isTestcafe') === 'yes'
    } catch (err) {
        // Absorb the error - not a big deal
        console.warn(err);
    }

    var experimentationVariation = getCookieValue(EXP_COOKIE_NAME);
    // Read from the cookie if it exists otherwise generate it yourself
    //  and write it to sticky them
    if (!experimentationVariation) {
        experimentationVariation = Math.random();
        var expirationDate = new Date((new Date()).getTime() + EXPIRATION_IN_DAYS * 24 * 60 * 60000);
        document.cookie = EXP_COOKIE_NAME + '=' + experimentationVariation + ';expires=' + expirationDate.toUTCString() + ';path=/;secure;';
    }

    if (
        !isTestcafe
    ){
        // (TODO) This logic will need to be updated for Prod
        var domain = (/^(www|rc)/).test(window.location.host) ? window.location.host : 'auto';

        // GA, good read: https://stackoverflow.com/questions/22716542/google-analytics-code-explanation

        // Taplytics + clickstream2BrowserId generation
        var first = document.getElementsByTagName('script')[0];
        var head = document.getElementsByTagName("head")[0];

        var loadUuidScript = document.createElement('script');
        loadUuidScript.src = 'https://assets.grubhub.com/assets/dll/load-uuid-d11fdcc95df7b83d07ef.js';

        window.taplyticsIdGlobal = '40d5efc3779f4354a9ca53f89d0d3605';
        var taplytics = document.createElement('script');
        taplytics.async = 1;
        taplytics.src = 'https://assets.grubhub.com/assets/dll/load-taplytics-7ac47c2429500a6067c5.js';
        var insertTaplyticsScript = function() {
            head.appendChild(taplytics);
        }
        // We'd like to load Taplytics after having uuid
        loadUuidScript.onload = insertTaplyticsScript;
        // If for any reason the uuid didn't load successfully, we still want to load Taplytics
        loadUuidScript.onerror = insertTaplyticsScript;

        head.insertBefore(loadUuidScript, head.firstChild);
    } else {
        // Disable AB testing and block in analytics
        window.ABTestingStatus = 'taplytics disabled';
        console.log('AB Testing is disabled');
    }
})();