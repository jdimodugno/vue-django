const Mutations = {
    login: `
        mutation ($username: String!, $password: String!) {
            login(username: $username, password: $password) {
                token {
                    key
                }
                user {
                    id
                    firstName
                    lastName
                }
            }
        }
    `,
    rateBeer: `
        mutation ($beerId: ID! $score: Int!, $userId: Int!) {
            createBeerRating(beerId: $beerId, score: $score, userId: $userId) {
                ok
            }
        }
    `
}

export default Mutations;
