export const WRITERS = [
 {
  "slug": "peyton-davison",
  "name": "Peyton Davison",
  "initials": "PD",
  "bio": "Peyton Davison is a writer covering AI and recruitment for RecruitmentAI.org, with a focus on sourcing and candidate outreach tools."
 },
 {
  "slug": "liam-hannon",
  "name": "Liam Hannon",
  "initials": "LH",
  "bio": "Liam Hannon is a writer covering AI and recruitment for RecruitmentAI.org, with a focus on applicant tracking, screening and interview software."
 },
 {
  "slug": "hunter-connor",
  "name": "Hunter Connor",
  "initials": "HC",
  "bio": "Hunter Connor is a writer covering AI and recruitment for RecruitmentAI.org, with a focus on AI agents and assistants in hiring."
 },
 {
  "slug": "robert-curry",
  "name": "Robert Curry",
  "initials": "RC",
  "bio": "Robert Curry is a writer covering AI and recruitment for RecruitmentAI.org, with a focus on recruiting software pricing and hiring stacks."
 }
];
const SITE = 'https://recruitmentai.org';
export function writerFor(path: string) { let h = 0; for (const c of path) h = (h * 31 + c.charCodeAt(0)) >>> 0; return WRITERS[h % WRITERS.length]; }
export const personLd = (w: { slug: string; name: string }) => ({ '@type': 'Person', name: w.name, url: `${SITE}/authors/${w.slug}/` });
