import Vue from 'vue';
import Router from 'vue-router';
import Home from 'Components/Home';
import Beers from 'Components/Beers';

Vue.use(Router);

const AppRouter = new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        }, {
            path: '/beers/',
            name: 'beers',
            component: Beers
        }/* __route__ */
    ]
});

export default AppRouter;
