<template>
  <div>
    <!-- search input -->
    <section id="knowledge-base-search">
      <b-card
        no-body
        class="knowledge-base-bg text-center"
        :style="{backgroundImage: `url(${require('@/assets/images/banner/banner.png')})`}"
      >
        <b-card-body class="card-body">
          <h2 class="text-primary">
            One place for all your Financial Search Needs.
          </h2>
          <b-card-text class="mb-2">
            <span>Popular searches: </span>
            <span class="font-weight-bolder">Loans, Insurance & Investments</span>
          </b-card-text>

          <!-- form -->
          <b-form class="kb-search-input">
            <b-input-group class="input-group-merge">
              <b-input-group-prepend is-text>
                <feather-icon icon="SearchIcon" />
              </b-input-group-prepend>
              <b-form-input
                v-model="SearchQuery"
                placeholder="Ask a question...."
                required
              />
            </b-input-group>
            <b-button
              v-ripple.400="'rgba(255, 255, 255, 0.15)'"
              variant="primary"
              style="margin-top: 2rem;"
              :disabled="SearchQuery.length===0"
              @click="getBlogs"
            >
              <feather-icon
                icon="SearchIcon"
                class="mr-50"
              />
              <span class="align-middle">Search</span>
            </b-button>
          </b-form>
          <!-- form -->
        </b-card-body>
      </b-card>
    </section>
    <!--/ search input -->
    <b-row
      class="container"
    >
      <b-row class="blog-list-wrapper">
        <h1 style="margin-bottom:40px;font-weight: bold; ">
          Blogs Search Results
        </h1>
        <h2
          v-if="empty"
          style="margin-left:2rem;"
        >
          No Blogs found for this query.
        </h2>
      </b-row>
      <b-row class="blog-list-wrapper">
        <b-col
          v-for="blog in blogLists"
          :key="blog.question"
          md="6"
        >
          <b-card
            tag="article"
            no-body
          >
            <b-link
              :href="blog.url"
              target="__blank"
            >
              <b-img
                :src="blog.imgUrl"
                class="card-img-top"
              />
            </b-link>
            <b-card-body>
              <b-card-title>
                <b-link
                  :href="blog.url"
                  class="blog-title-truncate text-body-heading"
                  target="__blank"
                >
                  {{ blog.question }}
                </b-link>
              </b-card-title>
              <div class="my-1 py-25">
                <b-link
                  v-for="tags in blog.keywords"
                  :key="tags"
                >
                  <b-badge
                    pill
                    class="mr-75"
                    variant="primary"
                  >
                    {{ tags }}
                  </b-badge>
                </b-link>
              </div>
              <b-card-text class="blog-content-truncate">
                {{ blog.body }}
              </b-card-text>
              <hr>
              <div class="d-flex justify-content-between align-items-center">
                <b-link
                  :href="blog.url"
                  target="__blank"
                  class="font-weight-bold"
                >
                  Read More
                </b-link>
              </div>
            </b-card-body>
          </b-card>
        </b-col>
      </b-row>
      <section id="knowledge-base-content">
        <!-- content -->
        <b-row class="kb-search-content-info match-height">
          <h1 style="margin-bottom:40px;font-weight: bold; ">
            FAQs by Category
          </h1>
        </b-row>
        <b-row class="kb-search-content-info match-height">
          <b-col
            v-for="item in filteredKB"
            :key="item.title"
            md="4"
            sm="6"
            class="kb-search-content"
          >
            <b-card
              class="text-center cursor-pointer"
              :img-src="item.img"
              img-top
              @click="$router.push({ name: 'pages-knowledge-base-category', params: { category: item.category } })"
            >
              <h4>{{ item.title }}</h4>
              <b-card-text class="mt-1">
                {{ item.desc }}
              </b-card-text>
            </b-card>
          </b-col>
          <b-col
            v-show="!filteredKB.length"
            cols="12"
            class="text-center"
          >
            <h4 class="mt-4">
              Search result not found!!
            </h4>
          </b-col>
        </b-row>
      </section>
    </b-row>

  </div>
</template>
<style scoped>
.container{
  margin: auto!important;
}
</style>
<script>
import {
  BRow, BCol, BButton, BCard, BCardBody, BForm, BCardTitle, BInputGroup, BFormInput, BCardText, BInputGroupPrepend, BImg, BLink, BBadge,
} from 'bootstrap-vue'
import { kFormatter } from '@core/utils/filter'
import axios from 'axios'

export default {
  components: {
    BRow,
    BCol,
    BCard,
    BCardBody,
    BCardText,
    BCardTitle,
    BForm,
    BBadge,
    BInputGroupPrepend,
    BButton,
    // BMedia,
    // BAvatar,
    // BMediaAside,
    // BMediaBody,
    BLink,
    BInputGroup,
    BImg,
    BFormInput,
  },
  data() {
    return {
      SearchQuery: '',
      knowledgeBaseSearchQuery: '',
      kb: [
        {
          title: 'Loans',
          img: ' ',
          desc: ' ',
          category: '',
        },
        {
          title: 'Insurance',
          img: ' ',
          desc: ' ',
          category: '',
        },
        {
          title: 'Credit Cards',
          img: ' ',
          desc: ' ',
          category: '',
        },
        {
          title: 'EMI Stores',
          img: ' ',
          desc: ' ',
          category: '',
        },
        {
          title: 'EMI Cards',
          img: ' ',
          desc: ' ',
          category: '',
        },
      ],
      search_query: '',
      empty: false,
      blogLists: [],
      blogList: [
        {
          title: 'How Important Are Credit Card Statements?',
          img: 'http://localhost:8080/images/blog/blog1.jpg',
          link: 'https://www.bajajfinservmarkets.in/credit-card/articles/how-important-are-credit-card-statements.html',
          excerpt: 'Credit Cards have drastically changed the way we look at our finances. Time and again, they have brought premium products within our buying reach and with this, have taught us.Yet, there is more than what meets the eye here. Before this euphoric bull run began, Bitcoin was more or less holding in the same range for almost 3 years. ',
        },
        {
          title: 'Cryptocurrencies: Digital Gold or a Ponzi Scheme? Should you make it a part of your portfolio?',
          img: 'http://localhost:8080/images/blog/blog2.jpeg',
          link: 'https://www.bajajfinservmarkets.in/discover/journals/blogs/investment/cryptocurrencies-digital-gold-or-a-ponzi-scheme/',
          excerpt: 'If you had bought Bitcoin worth Rs. 10 Lakhs at the start of March in 2020, it would have been worth approximately Rs. 1.1 Crores in March of 2021, a span of just one year. This shows you how the demand for cryptocurrency is increasing multifold. Yet, there is more than what meets the eye here. Before this euphoric bull run began, Bitcoin was more or less holding in the same range for almost 3 years.',
        },
        {
          title: '7 Key Pillars of the Finserv MARKETS platform',
          img: 'http://localhost:8080/images/blog/blog3.jpg',
          link: 'https://www.bajajfinservmarkets.in/discover/expert-speak/technology/7-key-pillars-of-the-finserv-markets-platform/',
          excerpt: 'Finserv MARKETS is an award-winning digital financial services marketplace. We offer over 27 financial products to over a million customers. The products range across Loans, Insurance, Investment, and Payments. We have, also, recently embarked upon an open market strategy where a customer is offered a choice from various other financial partners, to get the best product as per his needs.',
        },
        {
          title: 'Life Insurance in Times of Pandemic',
          img: 'http://localhost:8080/images/blog/blog4.jpg',
          link: 'https://www.bajajfinservmarkets.in/discover/expert-speak/insurance/life-insurance-in-times-of-pandemic/',
          excerpt: 'At the beginning of this year, nobody could have imagined that a pandemic would affect lives across the globe and cause several deaths. This has not only affected people but also impacted the global economy. Moreover, with people losing their lives unexpectedly, their family’s future is being pushed into a financial threat. With such a growing uncertainty, life insurance plans such as term insurance policies have assumed paramount significance during the current situation.',
        },
      ],
      blogSidebar: {},
      currentPage: 1,
      perPage: 1,
      rows: 140,

    }
  },
  computed: {
    filteredKB() {
      const knowledgeBaseSearchQueryLower = this.knowledgeBaseSearchQuery.toLowerCase()
      return this.kb.filter(item => item.title.toLowerCase().includes(knowledgeBaseSearchQueryLower) || item.desc.toLowerCase().includes(knowledgeBaseSearchQueryLower))
    },
    // filteredBlogs() {
    //   const knowledgeBaseSearchQueryLower = this.knowledgeBaseSearchQuery.toLowerCase()
    //   return this.blogList(blog => blog.title.toLowerCase().includes(knowledgeBaseSearchQueryLower) || blog.desc.toLowerCase().includes(knowledgeBaseSearchQueryLower))
    // },
  },
  created() {
    // this.$http.get('/blog/list/data').then(res => { this.blogList = res.data })
    this.$http.get('/kb/data/knowledge_base').then(res => { this.kb = res.data })
  },
  methods: {
    getBlogs() {
      axios.get(`http://127.0.0.1:5000/search_beta?query=${this.SearchQuery}`).then(response => {
        console.log(response.data)
        if (response.data === undefined) {
          this.empty = true
        } else {
          if (response.data.hits.length === 0) {
            this.empty = true
            return
          }
          this.blogLists = response.data.hits
          this.empty = false
        }
      })
        .catch(error => {
          console.log(error)
        })
    },
    kFormatter,
    tagsColor(tag) {
      if (tag === 'Quote') return 'light-info'
      if (tag === 'Gaming') return 'light-danger'
      if (tag === 'Fashion') return 'light-primary'
      if (tag === 'Video') return 'light-warning'
      if (tag === 'Food') return 'light-success'
      return 'light-primary'
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/pages/page-knowledge-base.scss';
</style>
