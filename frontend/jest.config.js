/** @type {import('ts-jest').JestConfigWithTsJest} */
module.exports = {
	preset: "ts-jest",
	testEnvironment: "node",
	clearMocks: true,
	collectCoverage: true,
	coverageDirectory: "./coverage",
	passWithNoTests: true,
	setupFilesAfterEnv: ["<rootDir>/src/setupTests.js"],
};
