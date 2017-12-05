import Vue from 'vue';
import App from 'Components/App';
import router from './router'
import store from 'Services/store'
import filters from './filters'

Vue.filter('number', filters.number);
/* __filter__ */

// eslint-disable-next-line no-new
new Vue({
    el: '#app',
    router,
    store,
    render: h => h(App)
});
