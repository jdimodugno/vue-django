import Vue from 'vue';
import Component from 'vue-class-component';

@Component()
export default class App extends Vue {

    beforeMount () {
        if (window.localStorage.getItem('token')) this.$store.dispatch('recover');
    }

    get user () {
        return Boolean(this.$store.state.user);
    }

    authenticate () {
        this.$store.dispatch('login');
    }
}
