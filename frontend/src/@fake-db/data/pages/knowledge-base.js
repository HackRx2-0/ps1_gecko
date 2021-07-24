import mock from '@/@fake-db/mock'
/* eslint-disable global-require */
const data = {
  // knowledge base
  knowledgeBase: [
    {
      id: 1,
      category: 'sales-automation',
      img: require('@/assets/images/illustration/sales.svg'),
      title: 'Loans',
      desc: 'There is perhaps no better demonstration of the folly of image of our tiny world.',
    },
    {
      id: 2,
      category: 'marketing-automation',
      img: require('@/assets/images/illustration/marketing.svg'),
      title: 'Credit Cards',
      desc: 'Look again at that dot. That’s here. That’s home. That’s us. On it everyone you love.',
    },
    {
      id: 3,
      category: 'api-questions',
      img: require('@/assets/images/illustration/api.svg'),
      title: 'EMI Stores',
      desc: 'every hero and coward, every creator and destroyer of civilization.',
    },
    {
      id: 4,
      category: 'personalization',
      img: require('@/assets/images/illustration/personalization.svg'),
      title: 'Insurance',
      desc: 'It has been said that astronomy is a humbling and character experience.',
    },
    {
      id: 5,
      category: 'email-marketing',
      img: require('@/assets/images/illustration/email.svg'),
      title: 'Investment',
      desc: 'There is perhaps no better demonstration of the folly of human conceits.',
    },
    {
      id: 6,
      category: 'demand-generation',
      img: require('@/assets/images/illustration/demand.svg'),
      title: 'Bajaj Finserv EMI Network Card',
      desc: 'Competent means we will never take anything for granted.',
    },
  ],
  categoryData: [
    {
      id: 0,
      title: 'Personal Loans',
      icon: 'SettingsIcon',
      iconColor: 'text-primary',
      questions: [
        {
          id: 0,
          question: 'What is a Personal Loan?',
          slug: 'personal-loan',
          link: 'https://www.bajajfinservmarkets.in/loans/personal-loan.html#parentHorizontalTab1',
        },
        {
          id: 1,
          question: 'Types of Personal Loan?',
          slug: 'personal-loan-type',
          link: 'https://www.bajajfinservmarkets.in/loans/personal-loan.html#parentHorizontalTab1',
        },
        {
          id: 2,
          question: 'Am I eligible for personal loan?',
          slug: 'personal-loan-eligibility',
          link: 'https://www.bajajfinservmarkets.in/loans/personal-loan.html#parentHorizontalTab1',
        },
      ],
    },
    {
      id: 1,
      title: 'Business Loans',
      icon: 'LinkIcon',
      iconColor: 'text-success',
      questions: [
        {
          id: 0,
          question: 'What is a Business Loan?',
          slug: 'Business-loan',
          link: 'https://www.bajajfinservmarkets.in/loans/business-loan.html#parentHorizontalTab1',
        },
        {
          id: 1,
          question: 'What are the types of Business Loan?',
          slug: 'Business-loan-type',
          link: 'https://www.bajajfinservmarkets.in/loans/business-loan.html#parentHorizontalTab1',
        },
        {
          id: 2,
          question: 'What are the features and benefits of Business Loan?',
          slug: 'Business-loan-benefits',
          link: 'https://www.bajajfinservmarkets.in/loans/business-loan.html#parentHorizontalTab1',
        },
      ],
    },
    {
      id: 2,
      title: 'Home Loans',
      icon: 'FileTextIcon',
      iconColor: 'text-danger',
      questions: [
        {
          id: 0,
          question: 'What is a Home Loan?',
          slug: 'Home-loan',
          link: 'https://www.bajajfinservmarkets.in/loans/home-loan.html#parentHorizontalTab1',
        },
        {
          id: 1,
          question: 'What are the types of home Loans?',
          slug: 'Home-loan-types',
          link: 'https://www.bajajfinservmarkets.in/loans/home-loan.html#parentHorizontalTab1',
        },
        {
          id: 2,
          question: 'What are the home loan rejection reasons?',
          slug: 'home-loan-reject',
          link: 'https://www.bajajfinservmarkets.in/loans/home-loan.html#parentHorizontalTab1',
        },
      ],
    },
    {
      id: 3,
      title: 'Loan Against Property',
      icon: 'LockIcon',
      iconColor: 'text-warning',
      questions: [
        {
          id: 0,
          question: 'What are the Factors Affecting Loan Against Property Interest Rates?',
          slug: 'loan-against-property-interest',
          link: 'https://www.bajajfinservmarkets.in/loans/loan-against-property.html#parentHorizontalTab1',
        },
        {
          id: 1,
          question: 'How to apply for Loan Against Property?',
          slug: 'LAP-Application',
          link: 'https://www.bajajfinservmarkets.in/loans/loan-against-property.html#parentHorizontalTab1',
        },
        {
          id: 2,
          question: 'What is the eligibility of Loan Against Property?',
          slug: 'LAP-Eligibility',
          link: 'https://www.bajajfinservmarkets.in/loans/loan-against-property.html#parentHorizontalTab1',
        },
      ],
    },
    {
      id: 4,
      title: 'Two-Wheeler Loan',
      icon: 'SmartphoneIcon',
      iconColor: 'text-info',
      questions: [
        {
          id: 0,
          question: 'What are the Advantages of Applying for a Two-Wheeler Loan?',
          slug: 'how-do-i-download-the-android-app',
          link: 'https://www.bajajfinservmarkets.in/loans/two-wheeler-loan.html#parentHorizontalTab1',
        },
        {
          id: 1,
          question: 'What are the Two Wheeler Loan Fees & Charges?',
          slug: 'how-to-download-our-ipad-app',
          link: 'https://www.bajajfinservmarkets.in/loans/two-wheeler-loan.html#parentHorizontalTab1',
        },
        {
          id: 2,
          question: 'What are the Two Wheeler Loan Eligibility & Documents Required?',
          slug: 'where-can-i-upload-my-avatar',
          link: 'https://www.bajajfinservmarkets.in/loans/two-wheeler-loan.html#parentHorizontalTab1',
        },
      ],
    },
    {
      id: 5,
      title: 'Professional Loan',
      icon: 'InfoIcon',
      iconColor: '',
      questions: [
        {
          id: 0,
          question: 'Why do you need a Professional Loan?',
          slug: 'Professional-loan',
          link: 'https://www.bajajfinservmarkets.in/loans/professional-loan.html',
        },
        {
          id: 1,
          question: 'What are the Features of Professional Loan?',
          slug: 'Professional-loan-features',
          link: 'https://www.bajajfinservmarkets.in/loans/professional-loan.html',
        },
        {
          id: 2,
          question: 'What is the eligibility Criteria of Loan for Professionals?',
          slug: 'professional-loan-eligibility',
          link: 'https://www.bajajfinservmarkets.in/loans/professional-loan.html',
        },
      ],
    },
  ],
  questionData: {
    title: 'Why Was My Developer Application Rejected?',
    lastUpdated: '10 Dec 2018',
    relatedQuestions: [
      {
        id: 0,
        question: 'How Secure Is My Password?',
      },
      {
        id: 1,
        question: 'Can I Change My Username?',
      },
      {
        id: 2,
        question: 'Where Can I Upload My Avatar?',
      },
      {
        id: 3,
        question: 'How Do I Change My Timezone?',
      },
      {
        id: 4,
        question: 'How Do I Change My Password?',
      },
    ],
    // ! Here we have used require for image source but in API it shall be URL of live image, this is just for demo purpose
    content: `<p>It has been said that astronomy is a humbling and character-building experience. There is perhaps no better demonstration of the folly of human conceits than this distant image of our tiny world. To me, it underscores our responsibility to deal more kindly with one another, and to preserve and cherish the pale blue dot, the only home we’ve ever known. The Earth is a very small stage in a vast cosmic arena. Think of the rivers of blood spilled by all those generals and emperors so that, in glory and triumph, they could become the momentary masters of a fraction of a dot. Think of the endless cruelties visited by the inhabitants of one corner of this pixel on the scarcely distinguishable inhabitants of some other corner, how frequent their misunderstandings, how eager they are to kill one another, how fervent their hatreds.</p><p class="ql-align-center"><img class="img-fluid w-100" src="${require('@/assets/images/pages/kb-image.jpg')}"></p></p><h5>Houston</h5><p>that may have seemed like a very long final phase. The auto targeting was taking us right into a … crater, with a large number of big boulders and rocks … and it required … flying manually over the rock field to find a reasonably good area.</p><ul><li><a href="javascript:void(0)" rel="noopener noreferrer" >I am a stranger. I come in peace. Take me to your leader and there will be a massive reward for you in eternity.</a></li><li><a href="javascript:void(0)" rel="noopener noreferrer" >It’s just mind-blowingly awesome. I apologize, and I wish I was more articulate, but it’s hard to be articulate when your mind’s blown—but in a very good way.</a></li><li><a href="javascript:void(0)" rel="noopener noreferrer" >A good rule for rocket experimenters to follow is this</a></li></ul>`,
  },
  // category
}
/* eslint-disable global-require */
mock.onGet('/kb/data/knowledge_base').reply(() => [200, data.knowledgeBase])
mock.onGet('/kb/data/category').reply(() => [200, data.categoryData])
mock.onGet('/kb/data/question').reply(() => [200, data.questionData])
