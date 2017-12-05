const Queries = {
    getCurrentUser: `
        query ($token: String!) {
            currentUser(token: $token) {
                id
                firstName
                lastName
            }
        }
    `,
    getBeers: `{
        beers {
            id
            name
            description
            abv
            image
            score
            votes
        }
    }`
}

export default Queries;
