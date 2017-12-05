import Vue from 'vue';
import Component from 'vue-class-component';
import BeerRating from 'Components/BeerRating';

@Component({
    props: ['beer'],
    components: {
        BeerRating
    }
})
export default class Beer extends Vue {

}
