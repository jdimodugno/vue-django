import Vue from 'vue';
import Vuex from 'vuex';

import api from 'Services/api';
import Mutations from 'GraphQL/mutations';
import Queries from 'GraphQL/queries';

Vue.use(Vuex);

const graphQLResponseHandler = (response, key) => {
    return response.data.data[key];
}

export default new Vuex.Store({
    state: {
        beers: null,
        user: null
    },
    getters: {
        beerById: (state, getters) => (id) => {
            return state.beers.find(beer => beer.id === id)
        }
    },
    mutations: {
        setBeers (state, payload) {
            state.beers = payload;
        },
        setUser (state, payload) {
            state.user = payload;
        }
    },
    actions: {
        recover ({state, commit}) {
            api.post('/graphql', {
                query: Queries.getCurrentUser,
                variables: {
                    token: window.localStorage.getItem('token')
                }
            }).then((response) => {
                this.commit('setUser', graphQLResponseHandler(response, 'currentUser'));
            });
        },
        login ({state, commmit}) {
            api.post('/graphql', {
                query: Mutations.login,
                variables: {
                    username: 'nouser',
                    password: 'nopassword'
                }
            }).then((response) => {
                const loginBody = graphQLResponseHandler(response, 'login');
                this.commit('setUser', loginBody.user);
                window.localStorage.setItem('token', loginBody.token.key);
            })
        },
        fetchBeers ({ state, commit }) {
            api.post('/graphql', {
                query: Queries.getBeers
            }).then((response) => {
                commit('setBeers', graphQLResponseHandler(response, 'beers'))
            });
        },
        rateBeer ({state, commit, dispatch}, payload) {
            console.log(state)
            api.post('/graphql', {
                query: Mutations.rateBeer,
                variables: {
                    beerId: payload.beerId,
                    score: payload.score,
                    userId: state.user.id
                }
            }).then((response) => dispatch('fetchBeers'));
        }
    }
});
