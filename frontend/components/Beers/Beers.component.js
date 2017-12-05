import Vue from 'vue';
import Component from 'vue-class-component';

import Beer from 'Components/Beer';

@Component({
    components: {
        Beer
    }
})
export default class Beers extends Vue {

    beforeMount () {
        this.$store.dispatch('fetchBeers');
    }

    get beers () {
        return this.$store.state.beers;
    }

    get loading () {
        return Boolean(this.$store.beers);
    }

    get title () {
        return 'Beers';
    }
}
