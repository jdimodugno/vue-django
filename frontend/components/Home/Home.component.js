import Vue from 'vue';
import Component from 'vue-class-component';

@Component()
export default class Home extends Vue {
    get title () {
        return 'Beer Lovers';
    }
}
