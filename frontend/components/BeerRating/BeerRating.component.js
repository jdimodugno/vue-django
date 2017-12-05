import Vue from 'vue';
import Component from 'vue-class-component';

@Component({
    props: ['beerId', 'score', 'votes']
})
export default class BeerRating extends Vue {
    rate (score) {
        this.$store.dispatch('rateBeer', {
            beerId: this.beerId,
            score
        })
    }
}
